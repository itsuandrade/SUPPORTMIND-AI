from sqlalchemy.orm import Session
from datetime import datetime, UTC

from backend.app.services.user.model import User

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def _get_by_id(self, id) -> User:
        user = self.db.query(User).filter(User.id == id).first()
        return user
    
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

    def list_all(self) -> list[User]:
        users = self.db.query(User).all()
        return users

    def get_by_attempt(self, attempt) -> User | None:        
        user = self.db.query(User).filter(User.username == attempt.username).first()
        return user
        
    def update(self, user, update) -> User:

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

    def delete(self, user) -> bool:
        self.db.delete(user)
        self.db.commit()
        return True