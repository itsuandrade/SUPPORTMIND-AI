from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketUpdate(BaseModel):
    category: str | None = None
    status: Literal['open', 'working on', 'closed'] | None = None
    priority: Literal['high', 'medium', 'low'] | None = None

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    status: Literal['open', 'working on', 'closed']
    priority: Literal['high', 'medium', 'low']
    created_at: datetime
    updated_at: datetime | None = None