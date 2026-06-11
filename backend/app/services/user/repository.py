from sqlalchemy.orm import Session
from datetime import datetime, UTC

from backend.app.services.user.model import User
from backend.app.services.user.schema import UserUpdate

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self,
               username: str,
               name: str,
               email: str,
               hashed_pw) -> User:

        user = User(
            username = username,
            name = name,
            email = email,
            hashed_pw = hashed_pw,
            role = 'user',
            created_at = datetime.now(UTC)
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def update(self, id: int, update) -> User:
        
        user = self.db.query(User).filter(User.id == id).first()

        if update.username:
            user.username = update.username

        if update.name:
            user.name = update.name

        if update.email:
            user.email = update.email

        if update.password:
            user.hashed_pw = update.password

        user.updated_at = datetime.now(UTC)

        self.db.commit()
        self.db.refresh(user)

        return user

    def delete(self, id) -> bool:

        user = self.db.query(User).filter(User.id == id).first()
        self.db.delete(user)
        self.db.commit()
        
        return True

    def list_all(self) -> list[User]:
        users = self.db.query(User).all()
        return users

    def get_by_id(self, id) -> User:
        user = self.db.query(User).filter(User.id == id).first()
        return user