"""The weather agent again, this time served with the official A2A Python SDK (a2a-sdk) and FastAPI.

Run it as:   python sdk_server.py        (port 9003)
"""
import uvicorn
from fastapi import FastAPI

from a2a.helpers import get_message_text, new_data_part, new_task_from_user_message, new_text_part
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import add_a2a_routes_to_fastapi, create_agent_card_routes, create_jsonrpc_routes
from a2a.server.tasks import InMemoryTaskStore, TaskUpdater
from a2a.types import AgentCapabilities, AgentCard, AgentInterface, AgentSkill, TaskState

from agent_brain import AGENTS, run_agent

PORT = 9003


# 1. The executor: the SDK calls execute() for every message; we only connect it to the brain
class WeatherExecutor(AgentExecutor):

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        task = context.current_task
        if task is None:                                              # a new task: announce it
            task = new_task_from_user_message(context.message)
            await event_queue.enqueue_event(task)
        updater = TaskUpdater(event_queue=event_queue, task_id=task.id, context_id=task.context_id)
        await updater.update_status(state=TaskState.TASK_STATE_WORKING)

        messages = [{"role": "system", "content": AGENTS["weather"]["prompt"]},
                    {"role": "user", "content": get_message_text(context.message)}]
        result = await run_agent("weather", messages)

        text_part = new_text_part(text=result["answer"], media_type="text/plain")
        data_part = new_data_part(data={"toolResults": result["tool_results"]}, media_type="application/json")
        await updater.add_artifact(parts=[text_part, data_part], name="weather-report")
        await updater.update_status(state=TaskState.TASK_STATE_COMPLETED)

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        raise NotImplementedError("This agent cannot cancel a task.")


# 2. The Agent Card, built from the SDK's types (they follow the A2A 1.0 data model)
skill = AgentSkill(id="current-weather",
                   name="Current weather",
                   description="The current temperature and conditions of one or more cities.",
                   tags=["weather", "travel"],
                   examples=["What is the weather in Lahore right now?"])

agent_card = AgentCard(name="Weather Agent (SDK)",
                       description="The current temperature and conditions of one or more cities.",
                       version="1.0.0",
                       supported_interfaces=[AgentInterface(url=f"http://127.0.0.1:{PORT}/",
                                                            protocol_binding="JSONRPC",
                                                            protocol_version="1.0")],
                       capabilities=AgentCapabilities(streaming=True),
                       default_input_modes=["text/plain"],
                       default_output_modes=["text/plain", "application/json"],
                       skills=[skill])

# 3. The SDK's request handler does the protocol work: tasks, states, JSON-RPC, errors, streaming
request_handler = DefaultRequestHandler(agent_executor=WeatherExecutor(),
                                        task_store=InMemoryTaskStore(),
                                        agent_card=agent_card)

app = FastAPI(title="Weather Agent (SDK)")
add_a2a_routes_to_fastapi(app,
                          agent_card_routes=create_agent_card_routes(agent_card),
                          jsonrpc_routes=create_jsonrpc_routes(request_handler, rpc_url="/"))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=PORT, log_level="warning")
