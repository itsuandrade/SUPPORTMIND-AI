from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    name: str | None = None
    email: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    email: str
    role: str
    created_at: datetime
    updated_at: datetime | None = None