from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.services.user.schema import *
from backend.app.services.user.service import UserService

user_router = APIRouter(
    prefix='/user',
    tags=['Users']
)

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)

@user_router.get('/', response_model=list[UserResponse])
def get_users(user_service: UserService = Depends(get_user_service)):
    users = user_service.list_all()
    return users

@user_router.get('/{user_id}', response_model=UserResponse)
def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_by_id(user_id)
    return user

@user_router.post('/', response_model=UserResponse)
def create_user(new_user: UserCreate, user_service: UserService = Depends(get_user_service)):
    user = user_service.create_user(new_user)
    return user

@user_router.put('/{user_id}', response_model=UserResponse)
def update_user(user_id: int, update_user: UserUpdate, user_service: UserService = Depends(get_user_service)):
    user = user_service.update_user(id = user_id, update = update_user)
    return user

@user_router.delete('/{user_id}')
def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
    deleted = user_service.delete_user(user_id)

    if deleted:
        return {'message': f'User {user_id} deletado com sucesso.'}
    else:
        raise HTTPException(404, detail='Usuário não encontrado.')

# @user_router.post('/me')