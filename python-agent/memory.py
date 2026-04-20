# Simple in-memory store — swap for Redis when scaling
_sessions: dict = {}

def get_history(session_id: str) -> list:
    return _sessions.get(session_id, []).copy()

def save_history(session_id: str, history: list):
    # Keep last 20 messages to stay within context limits
    _sessions[session_id] = history[-20:]