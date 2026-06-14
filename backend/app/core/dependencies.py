from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import jwt

from dotenv import load_dotenv
import os
load_dotenv('.env')

from backend.app.services.user.model import User
from backend.app.core.database import get_db

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl='/users/login'
)

def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)) -> User:

    try:
        
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        print(payload)

        user_id = int(payload['sub'])
        
        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )
        
        if user is None:
            raise HTTPException(404, 'User not found.')
        
        return user

    except (jwt.ExpiredSignatureError, jwt.PyJWTError):
        raise HTTPException(401, 'Invalid token.')