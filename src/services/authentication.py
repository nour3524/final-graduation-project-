from passlib.context import CryptContext
from repositories import get_user
from datetime import timedelta
from typing import Optional
from datetime import datetime
from jose import JWTError, jwt
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
import os
from models import UserDataDTO, SystemAdmin
from repositories import get_user

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer_scheme = HTTPBearer()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(email: str, password: str) -> Optional[SystemAdmin]:
    user = get_user(email)
    if not user or not verify_password(password, user.PasswordHash):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))) or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt

def get_current_user(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        if payload is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = UserDataDTO(ID = payload["ID"], UserName = payload["UserName"], Name = payload["Name"])
    return user
    