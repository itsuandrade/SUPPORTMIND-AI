from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.core.dependencies import get_current_user
from backend.app.services.user.schema import *
from backend.app.services.user.model import User
from backend.app.services.user.service import UserService

user_router = APIRouter(
    prefix='/users',
    tags=['Users']
)

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)

#ATTEMPT LOGIN
@user_router.post('/login')
def attempt_login(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)):
    
    token = user_service.attempt_login(form_data)
    
    return TokenResponse(
        access_token = token,
        token_type = 'bearer'
    )

@user_router.get('/me', response_model=UserResponse)
def get_me(user: User = Depends(get_current_user)) -> User:
    return user

#USER CRUD:

@user_router.post('/', response_model=UserResponse)
def create_user(new_user: UserCreate,
                user_service: UserService = Depends(get_user_service)):
    
    user = user_service.create_user(new_user)
    return user

@user_router.get('/', response_model=list[UserResponse])
def get_users(user: User = Depends(get_current_user),
              user_service: UserService = Depends(get_user_service)) -> list[User]:
    
    users = user_service.list_all(user)
    return users

@user_router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, 
             user: User = Depends(get_current_user),
             user_service: UserService = Depends(get_user_service)) -> User:
    
    search_user = user_service.get_by_id(user, user_id)
    return search_user

@user_router.put('/', response_model=UserResponse)
def update_user(update_user: UserUpdate,
                user: User = Depends(get_current_user), 
                user_service: UserService = Depends(get_user_service)) -> User:
    
    updated_user = user_service.update_user(user, update_user)
    return updated_user

@user_router.delete('/')
def delete_user(user: User = Depends(get_current_user),
                user_service: UserService = Depends(get_user_service)):
    
    user_service.delete_user(user)
    return {'message': f'User deletado com sucesso.'}


