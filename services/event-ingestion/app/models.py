from pydantic import BaseModel, Field
from typing import Optional, Union, Dict, Any
from datetime import datetime

class Event(BaseModel):
    event_id: str = Field(..., description="Unique UUID for the event")
    user_id: Union[str, int]
    event_type: str
    page: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    ts: datetime = Field(..., description="ISO8601 timestamp, auto‑parsed into datetime")
