"""The "brain" of our A2A agents: the weather and hotels sub-agents of Lec-50, Section 4.

Both A2A servers import it: a2a_server.py (written from scratch) and sdk_server.py (written with the
official A2A SDK). The brain knows nothing about A2A; the servers know nothing about LLMs or MCP.
"""
import os
import json

from fastmcp import Client
from openai import AsyncOpenAI

MODEL = "openai/gpt-oss-20b"                        # the sub-agents' model, as in Section 4
MAX_STEPS = 6                                        # guardrail for every agent
NEED_INPUT = "NEED INPUT:"                           # how the brain tells its server that it needs more information

llm = AsyncOpenAI(api_key=os.getenv("GROQ_API_KEY"),
                  base_url="https://api.groq.com/openai/v1",
                  max_retries=5)

AGENTS = {
    "weather": {
        "url": "https://mcp-render-server-xzbh.onrender.com/mcp",      # our Demo-server (Lec-46)
        "tools": ["get_weather"],
        "prompt": "You are a weather specialist. Use get_weather for every city in the task. Reply in at most 3 short lines: "
                  "the temperature in °C and the conditions for each city. Report only what the tool returned. "
                  f"If the task names no city, do not call the tool: reply with '{NEED_INPUT}' and one short question.",
    },
    "hotels": {
        "url": "https://booking-mcp-server.onrender.com/mcp",           # the Booking server (Lec-46)
        "tools": ["search_hotels"],
        "prompt": "You are a hotel specialist. Use search_hotels with exactly the city, dates and number of adults in the task. "
                  "Reply with the 3 cheapest hotels, one line each: name, price in USD as given by the tool, and rating. "
                  "Report only what the tool returned; if the task asks for anything else, say that it is not available. "
                  f"If the task does not give the city, both dates and the number of adults, do not call the tool: "
                  f"reply with '{NEED_INPUT}' and one short question.",
    },
}


async def run_agent(agent_name, messages):
    """The agent loop of Section 4, for one agent and one conversation.

    Returns a dict with the final answer, the tool results the agent read, and the tokens it used.
    """
    spec = AGENTS[agent_name]
    tool_results = []
    tokens = 0
    async with Client(spec["url"], timeout=120) as mcp:
        tool_schemas = []
        for tool in await mcp.list_tools():
            if tool.name in spec["tools"]:                                # least privilege
                tool_schemas.append({"type": "function",
                                     "function": {"name": tool.name,
                                                  "description": tool.description,
                                                  "parameters": tool.input_schema}})

        for step in range(MAX_STEPS):
            response = await llm.chat.completions.create(model=MODEL, messages=messages, tools=tool_schemas)
            tokens = tokens + response.usage.total_tokens
            message = response.choices[0].message
            messages.append(message)

            if not message.tool_calls:                                    # no tool calls: the agent has answered
                if message.content:
                    return {"answer": message.content, "tool_results": tool_results, "tokens": tokens}
                messages.append({"role": "user", "content": "Your last reply was empty. Please continue."})
                continue

            for tool_call in message.tool_calls:
                arguments = json.loads(tool_call.function.arguments)
                result = await mcp.call_tool(tool_call.function.name, arguments, raise_on_error=False)
                if result.content:
                    text = result.content[0].text
                else:
                    text = "(no output)"
                messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": text})
                try:
                    data = json.loads(text)                               # keep the raw result as data, if it is JSON
                except json.JSONDecodeError:
                    data = text
                tool_results.append({"tool": tool_call.function.name, "arguments": arguments, "result": data})

    return {"answer": f"Stopped after {MAX_STEPS} steps without a final answer.", "tool_results": tool_results, "tokens": tokens}
