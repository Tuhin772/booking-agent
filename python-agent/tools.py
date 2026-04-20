import httplib2

NODE_API = "http://localhost:3000/api"

TOOLS = [
    {
        "name": "check_slots",
        "description": "Check available appointment slots for a given date",
        "input_schema": {
            "type": "object",
            "properties": {
                "date": { "type": "string", "description": "Date in YYYY-MM-DD format" }
            },
            "required": ["date"]
        }
    },
    {
        "name": "create_booking",
        "description": "Book an appointment for a customer",
        "input_schema": {
            "type": "object",
            "properties": {
                "name":    { "type": "string" },
                "email":   { "type": "string" },
                "date":    { "type": "string" },
                "time":    { "type": "string" },
                "service": { "type": "string" }
            },
            "required": ["name", "email", "date", "time", "service"]
        }
    },
    {
        "name": "cancel_booking",
        "description": "Cancel an existing booking by booking ID",
        "input_schema": {
            "type": "object",
            "properties": {
                "booking_id": { "type": "string" }
            },
            "required": ["booking_id"]
        }
    }
]

import httpx

async def handle_tool(name: str, inputs: dict) -> str:
    async with httpx.AsyncClient() as client:
        if name == "check_slots":
            r = await client.get(f"{NODE_API}/slots", params=inputs)
            return r.text
        elif name == "create_booking":
            r = await client.post(f"{NODE_API}/bookings", json=inputs)
            return r.text
        elif name == "cancel_booking":
            r = await client.delete(f"{NODE_API}/bookings/{inputs['booking_id']}")
            return r.text
    return "Tool not found"