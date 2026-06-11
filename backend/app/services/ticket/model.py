from backend.app.core.database import Base
from sqlalchemy import Column, String, Integer, DateTime

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)

    category = Column(String, nullable=False)
    status = Column(String, nullable=False)
    priority = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    test_column = Column(String, nullable=True)