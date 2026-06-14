from datetime import datetime, timedelta, UTC
import jwt
import bcrypt as bc

from dotenv import load_dotenv
import os
load_dotenv('.env')

#ENV and variables:
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_TOKEN_EXPIRE_MINUTES = 10

#Password
def hash_password(password: str):
    pw = password.encode('utf-8')
    hashed_pw = bc.hashpw(pw, bc.gensalt())
    return hashed_pw

def check_password(pw: str, hashed_pw: str):

    check = bc.checkpw(
        pw.encode('utf-8'),
        hashed_pw.encode('utf-8')
    )

    return check

#Get JWT token
def create_access_token(user_id):

    expire_time = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_TOKEN_EXPIRE_MINUTES)
    payload = {
        'sub': str(user_id),
        'exp': expire_time
    }

    token = jwt.encode(payload, key=SECRET_KEY, algorithm=ALGORITHM)

    return token

