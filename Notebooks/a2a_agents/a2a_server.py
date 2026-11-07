"""An A2A server written from scratch with FastAPI (A2A v1.0, JSON-RPC binding).

Run it as:   python a2a_server.py weather 9001      or      python a2a_server.py hotels 9002
"""
import os
import sys
import uuid
from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from agent_brain import AGENTS, NEED_INPUT, run_agent

AGENT_NAME = sys.argv[1]                                  # "weather" or "hotels"
PORT = int(sys.argv[2])                                   # 9001 or 9002
API_KEY = os.getenv("A2A_API_KEY", "my-class-key")        # clients must send it in the X-API-Key header

# ================================================================
# 1. The Agent Card: who this agent is, where it lives, how to call it, and what it can do
# ================================================================
SKILLS = {
    "weather": {"id": "current-weather",
                "name": "Current weather",
                "description": "The current temperature and conditions of one or more cities.",
                "tags": ["weather", "travel"],
                "examples": ["What is the weather in Lahore right now?"]},
    "hotels":  {"id": "hotel-search",
                "name": "Hotel search",
                "description": "The cheapest hotels of a city for given check-in and check-out dates and a number of adults.",
                "tags": ["hotels", "travel", "booking"],
                "examples": ["Find the 3 cheapest hotels in Lahore for 2 adults from 2026-11-16 to 2026-11-18."]},
}

AGENT_CARD = {
    "name": f"{AGENT_NAME.title()} Agent",
    "description": SKILLS[AGENT_NAME]["description"],
    "version": "1.0.0",
    "provider": {"organization": "Lec-50 Travel Demo", "url": "https://github.com/arifpucit/Generative-and-Agentic-AI"},
    "supportedInterfaces": [{"url": f"http://127.0.0.1:{PORT}/",           # where to send JSON-RPC requests
                             "protocolBinding": "JSONRPC",
                             "protocolVersion": "1.0"}],
    "capabilities": {"streaming": False, "pushNotifications": False},
    "securitySchemes": {"apiKey": {"apiKeySecurityScheme": {"location": "header", "name": "X-API-Key"}}},
    "securityRequirements": [{"schemes": {"apiKey": {"list": []}}}],
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain", "application/json"],
    "skills": [SKILLS[AGENT_NAME]],
}

# ================================================================
# 2. Task storage: the Task the client sees, and the LLM conversation only the server sees
# ================================================================
TASKS = {}                     # task id -> Task
CONVERSATIONS = {}             # task id -> the brain's messages list (kept for multi-turn tasks)
FINAL_STATES = ["TASK_STATE_COMPLETED", "TASK_STATE_FAILED", "TASK_STATE_CANCELED", "TASK_STATE_REJECTED"]


def now():
    """The current time as an ISO 8601 UTC timestamp, as the spec requires."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def agent_message(task, text):
    """A Message from this agent (role ROLE_AGENT) that belongs to the given task."""
    return {"messageId": str(uuid.uuid4()),
            "role": "ROLE_AGENT",
            "taskId": task["id"],
            "contextId": task["contextId"],
            "parts": [{"text": text}]}


def rpc_result(request_id, result):
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def rpc_error(request_id, code, message):
    return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


# ================================================================
# 3. The two operations this agent supports: SendMessage and GetTask
# ================================================================
async def send_message(request_id, message):
    task_id = message.get("taskId")
    if task_id is None:                                                    # a new task
        task_id = str(uuid.uuid4())
        TASKS[task_id] = {"id": task_id,
                          "contextId": message.get("contextId", str(uuid.uuid4())),
                          "status": {"state": "TASK_STATE_SUBMITTED", "timestamp": now()},
                          "artifacts": [],
                          "history": [],
                          "metadata": {"tokens": 0}}
        CONVERSATIONS[task_id] = [{"role": "system", "content": AGENTS[AGENT_NAME]["prompt"]}]
    elif task_id not in TASKS:
        return rpc_error(request_id, -32001, "Task not found")

    task = TASKS[task_id]
    if task["status"]["state"] in FINAL_STATES:
        return rpc_error(request_id, -32004, "The task is already finished and accepts no more messages")

    # The client's message joins the task's history, and its text goes to the brain
    task["history"].append(message)
    task["status"] = {"state": "TASK_STATE_WORKING", "timestamp": now()}
    text = ""
    for part in message["parts"]:
        if "text" in part:
            text = text + part["text"]
    CONVERSATIONS[task_id].append({"role": "user", "content": text})

    try:
        result = await run_agent(AGENT_NAME, CONVERSATIONS[task_id])
    except Exception as error:                                             # a failed agent becomes a failed task
        task["status"] = {"state": "TASK_STATE_FAILED", "message": agent_message(task, f"Error: {error}"), "timestamp": now()}
        return rpc_result(request_id, {"task": task})
    task["metadata"]["tokens"] = task["metadata"]["tokens"] + result["tokens"]

    answer = result["answer"]
    if answer.startswith(NEED_INPUT):                                      # the brain needs more information
        question = agent_message(task, answer[len(NEED_INPUT):].strip())
        task["history"].append(question)
        task["status"] = {"state": "TASK_STATE_INPUT_REQUIRED", "message": question, "timestamp": now()}
    else:                                                                  # the result goes into an Artifact
        artifact = {"artifactId": str(uuid.uuid4()),
                    "name": f"{AGENT_NAME}-report",
                    "parts": [{"text": answer, "mediaType": "text/plain"},
                              {"data": {"toolResults": result["tool_results"]}, "mediaType": "application/json"}]}
        task["artifacts"].append(artifact)
        task["status"] = {"state": "TASK_STATE_COMPLETED", "timestamp": now()}
    return rpc_result(request_id, {"task": task})


# ================================================================
# 4. The web server: one GET route for the card, one POST route for every JSON-RPC request
# ================================================================
app = FastAPI(title=AGENT_CARD["name"])


@app.get("/.well-known/agent-card.json")
async def get_agent_card():
    return AGENT_CARD                                                      # public: no API key needed


@app.post("/")
async def json_rpc(request: Request):
    body = await request.json()
    request_id = body.get("id")

    if request.headers.get("X-API-Key") != API_KEY:                        # authentication (HTTP level)
        return JSONResponse(status_code=401, content={"detail": "Missing or wrong X-API-Key header"})
    if request.headers.get("A2A-Version") != "1.0":                        # version negotiation
        return rpc_error(request_id, -32009, "Version not supported: this agent speaks A2A 1.0")

    method = body.get("method")
    params = body.get("params", {})
    if method == "SendMessage":
        return await send_message(request_id, params["message"])
    if method == "GetTask":
        if params.get("id") not in TASKS:
            return rpc_error(request_id, -32001, "Task not found")
        return rpc_result(request_id, TASKS[params["id"]])
    return rpc_error(request_id, -32601, f"Method not found: {method}")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT, log_level="warning")
