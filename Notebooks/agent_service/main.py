import os
import json
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from fastmcp import Client
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

# On your laptop the keys come from a local .env file; on Render they come from
# the service's Environment Variables (a missing .env file is simply ignored).
load_dotenv()

MODEL = "openai/gpt-oss-120b"
MAX_STEPS = 6                                     # guardrail: a server must never loop forever
AGENT_API_TOKEN = os.getenv("AGENT_API_TOKEN")    # if set, clients must send "Authorization: Bearer <token>"

SYSTEM_PROMPT = """You are a helpful travel assistant. Use the tools whenever they help to answer the user's question,
then answer briefly."""

# AsyncOpenAI: while one request waits for Groq, the server can work on other requests.
# max_retries: wait and try again when Groq answers 429 (rate limit), instead of failing at once.
llm = AsyncOpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1",
                  timeout=60, max_retries=5)


# ================================================================
# 1. The tools live on two remote MCP servers: our Demo-server (Lec-46) and the Booking server
# ================================================================
MCP_SERVERS = {
    "mcpServers": {
        "demo":    {"url": "https://mcp-render-server-xzbh.onrender.com/mcp"},
        "booking": {"url": "https://booking-mcp-server.onrender.com/mcp"},
    }
}
mcp_client = Client(MCP_SERVERS, timeout=120)


def mcp_tools_to_schemas(mcp_tools):
    """Convert MCP tools into the function-tool format the LLM expects (Lec-47, unchanged)."""
    return [{"type": "function",
             "function": {"name": tool.name, "description": tool.description, "parameters": tool.input_schema}}
            for tool in mcp_tools]


# ================================================================
# 2. Run one tool call on the MCP server (Lec-47, unchanged)
# ================================================================
async def run_tool(tool_call):
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)
    print(f"  tool: {name}({args})", flush=True)                     # shows up in Render's Logs tab
    result = await mcp_client.call_tool(name, args, raise_on_error=False)
    return result.content[0].text if result.content else "(no output)"


# ================================================================
# 3. The agent loop (Lec-47) with two changes: `await llm...` and at most MAX_STEPS rounds
# ================================================================
async def run_agent(messages):
    tool_calls = []                                                   # what the agent did, sent back to the client
    for step in range(MAX_STEPS):
        response = await llm.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
        )
        message = response.choices[0].message
        messages.append(message)

        # No tool calls means the model is done and answered in plain text
        if not message.tool_calls:
            return message.content, tool_calls

        for tool_call in message.tool_calls:
            result = await run_tool(tool_call)
            tool_calls.append(f"{tool_call.function.name}({tool_call.function.arguments})")
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })
    return f"Sorry, I stopped after {MAX_STEPS} steps without a final answer.", tool_calls


# ================================================================
# 4. The web service: replaces Lec-47's `while True: input()` chat loop
# ================================================================
sessions = {}                       # session_id -> that user's messages (kept in memory, lost on restart)


@asynccontextmanager
async def lifespan(app):
    """Runs once: connect to the MCP servers when the service starts, disconnect when it stops."""
    global TOOL_SCHEMAS
    async with mcp_client:
        TOOL_SCHEMAS = mcp_tools_to_schemas(await mcp_client.list_tools())
        print(f"Agent ready with {len(TOOL_SCHEMAS)} tools from {len(MCP_SERVERS['mcpServers'])} MCP servers", flush=True)
        yield                       # the service answers requests while we wait here


app = FastAPI(title="Travel Agent", lifespan=lifespan)


class ChatRequest(BaseModel):
    session_id: str
    message: str = Field(max_length=2000)          # guardrail: refuse very long messages


@app.get("/health")
async def health():
    return {"status": "ok", "model": MODEL, "tools": len(TOOL_SCHEMAS), "sessions": len(sessions)}


@app.post("/chat")
async def chat(request: ChatRequest, authorization: str = Header(default="")):
    # 1. Only clients that know the token may spend our Groq quota
    if AGENT_API_TOKEN and authorization != f"Bearer {AGENT_API_TOKEN}":
        raise HTTPException(status_code=401, detail="Missing or wrong token")

    # 2. This session's conversation so far (a new session starts with the system prompt), plus the new message
    history = sessions.get(request.session_id, [{"role": "system", "content": SYSTEM_PROMPT}])
    messages = history + [{"role": "user", "content": request.message}]

    # 3. Run the agent; if Groq or an MCP server fails, send back a clear error instead of crashing
    print(f"[{request.session_id}] {request.message}", flush=True)
    try:
        reply, tool_calls = await run_agent(messages)
    except Exception as error:
        raise HTTPException(status_code=503, detail=f"The agent failed: {error}")

    # 4. Remember the conversation (only when the agent succeeded) and answer in JSON
    sessions[request.session_id] = messages
    return {"session_id": request.session_id, "reply": reply, "tool_calls": tool_calls}


if __name__ == "__main__":
    # Render tells the app which port to use through the PORT variable; on your laptop it is 8000.
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
