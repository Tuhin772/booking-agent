import anthropic
from tools import TOOLS, handle_tool
from memory import get_history, save_history

client = anthropic.Anthropic()

SYSTEM = """You are a friendly appointment booking assistant.
Your job is to help customers book, reschedule, or cancel appointments.
Always confirm the date, time, and service before booking.
Be concise and warm."""

async def run_agent(session_id: str, user_message: str) -> str:
    history = get_history(session_id)
    history.append({ "role": "user", "content": user_message })

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=SYSTEM,
            tools=TOOLS,
            messages=history
        )

        history.append({ "role": "assistant", "content": response.content })

        if response.stop_reason == "end_turn":
            save_history(session_id, history)
            return response.content[0].text

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = await handle_tool(block.name, block.input)
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            history.append({ "role": "user", "content": tool_results })