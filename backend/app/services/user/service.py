from backend.app.services.user.repository import UserRepository
from sqlalchemy.orm import Session

class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, new_user):
        
        user = self.repository.create(
            username = new_user.username,
            name = new_user.name,
            email = new_user.email,
            hashed_pw = new_user.password
        )

        return user
    
    def update_user(self, id: int, update):
        
        user = self.repository.update(id = id, update = update)

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