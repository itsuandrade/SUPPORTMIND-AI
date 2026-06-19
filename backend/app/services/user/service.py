from sqlalchemy.orm import Session

from backend.app.services.user.model import User
from backend.app.services.user.repository import UserRepository
from backend.app.services.user.permissions import UserPermissionService
from backend.app.services.user.exceptions import UserNotFound, WrongCredentials
from backend.app.core.security import hash_password, check_password, create_access_token


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.permission = UserPermissionService()

    def _get_user_or_raise(self, id):

        user = self.repository._get_by_id(id)

        if not user:
            raise UserNotFound()
        
        return user

    def create_user(self, new_user) -> User:
        
        hashed_password = hash_password(new_user.password)
        hashed_pw = hashed_password.decode('utf-8')

        user = self.repository.create(
            username = new_user.username,
            name = new_user.name,
            email = new_user.email,
            hashed_pw = hashed_pw
        )

        return user
    
    def list_all(self, user):
        self.permission.validate_admin(user)
        users = self.repository.list_all()
        return users
    
    def get_by_id(self, user, id) -> User:
        self.permission.validate_admin(user)
        search_user = self._get_user_or_raise(id)
        return search_user
    
    def update_user(self, user, update) -> User:

        if update.password:
            hashed_pw = hash_password(update.password).decode('utf-8')
            update.password = hashed_pw

        updated_user = self.repository.update(user, update)

        return updated_user

    def delete_user(self, user):
        deleted = self.repository.delete(user)
        return deleted

    def attempt_login(self, attempt) -> str | None:
        
        user = self.repository.get_by_attempt(attempt)

        if not user:
            raise WrongCredentials()
        
        if not check_password(attempt.password, user.hashed_pw):
            raise WrongCredentials()

        token = create_access_token(user.id)
        return token


