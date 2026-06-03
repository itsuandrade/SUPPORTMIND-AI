from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class Ticket(BaseModel):
    title: str
    description: str
    status: Literal['open', 'working on', 'closed']
    priority: Literal['high', 'medium', 'low']
    created_at: datetime
    updated_at: datetime | None = None