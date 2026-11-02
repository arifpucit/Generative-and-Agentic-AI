# agent_service (Lec-48)

The Lec-47 MCP-powered agent, served over HTTP with FastAPI so that any program can talk to it.

- `POST /chat` with `{"session_id": "...", "message": "..."}` and the header `Authorization: Bearer <AGENT_API_TOKEN>`
- `GET /health` for Render's health check

Run locally: `uv run main.py`, then open http://127.0.0.1:8000/docs

Deploy on Render: Build Command `uv sync --frozen && uv cache prune --ci`, Start Command `uv run main.py`,
environment variables `GROQ_API_KEY` and `AGENT_API_TOKEN`, health check path `/health`.
