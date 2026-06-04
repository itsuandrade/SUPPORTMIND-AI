from backend.app.core.database import Base
from sqlalchemy import Column, String, Integer, DateTime

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    description = Column(String)

    category = Column(String)
    status = Column(String)
    priority = Column(String)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)