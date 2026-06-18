from backend.app.core.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True, nullable=False)
    hashed_pw = Column(String, nullable=False)
    role = Column(String, nullable=False)

    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    tickets = relationship(
        "Ticket",
        back_populates = 'user',
        cascade='all, delete-orphan'
    )