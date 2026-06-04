from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketUpdate(BaseModel):
    category: str
    status: Literal['open', 'working on', 'closed']
    priority: Literal['high', 'medium', 'low']  