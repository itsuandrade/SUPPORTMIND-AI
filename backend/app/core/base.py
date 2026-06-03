from database import Base
from sqlalchemy import Column, String, Integer, DateTime

class Tickets(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    status = Column(String)
    priority = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)