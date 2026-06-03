from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketUpdate(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None
    updated_at: str  # Não sei a melhor forma de guardar essa informação, chat...

class TicketDelete(BaseModel):
    id: int
    updated_at: str  # Não sei a melhor forma de guardar essa informação, chat...