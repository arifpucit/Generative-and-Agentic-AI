# a2a_agents (Lec-50, Section 9)

The weather and hotels sub-agents of Lec-50 as A2A servers (A2A protocol v1.0, JSON-RPC binding).
The notebook writes the three Python files with `%%writefile` and starts the servers itself.

- `agent_brain.py`: the sub-agents (system prompt, gpt-oss-20b, agent loop, one MCP tool each). Knows nothing about A2A.
- `a2a_server.py`: an A2A server written from scratch with FastAPI. `python a2a_server.py weather 9001` or `python a2a_server.py hotels 9002`.
- `sdk_server.py`: the weather agent served with the official A2A Python SDK (`a2a-sdk`) and FastAPI: `python sdk_server.py` (port 9003).

All three run in the course environment (`a2a-sdk[http-server]` is in the course `pyproject.toml`).
The servers read `GROQ_API_KEY` from the environment. Clients of `a2a_server.py` must send the header `X-API-Key`
(default `my-class-key`, or the value of `A2A_API_KEY`) and `A2A-Version: 1.0`. Agent Card: `GET /.well-known/agent-card.json`.
