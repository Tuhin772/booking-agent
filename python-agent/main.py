from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    session_id: str

@app.post("/agent")
async def agent_endpoint(req: ChatRequest):
    reply = await run_agent(req.session_id, req.message)
    return { "reply": reply, "session_id": req.session_id }