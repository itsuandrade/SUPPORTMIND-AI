from sqlalchemy.orm import Session

from backend.app.services.user.repository import UserRepository
from backend.app.core.security import hash_password, check_password, create_access_token

class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, new_user):
        
        hashed_password = hash_password(new_user.password)
        hashed_pw = hashed_password.decode('utf-8')

        user = self.repository.create(
            username = new_user.username,
            name = new_user.name,
            email = new_user.email,
            hashed_pw = hashed_pw
        )

        return user
    
    def update_user(self, id: int, update):
        
        if update.password:
            hashed_pw = hash_password(update.password).decode('utf-8')
            update.hashed_pw = hashed_pw

        user = self.repository.update(id, update)

        return user

    def delete_user(self, id: int):

        deleted = self.repository.delete(id)

        return deleted

    def list_all(self):
        users = self.repository.list_all()
        return users
    
    def get_by_id(self, id):
        user = self.repository.get_by_id(id)
        return user
    
    def attempt_login(self, attempt) -> str | None:
        
        if attempt.username:
            user = self.repository.get_by_attempt(attempt)
        else: 
            return None

        if not user:
            return None
        
        if check_password(attempt.password, user.hashed_pw):
            token = create_access_token(user.id)
            return token


