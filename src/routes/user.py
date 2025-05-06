import uvicorn
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
import os
from common import map_user_to_dict
from models import UserSignInVM, UserSignUpVM, AddUserDTO
from services.authentication import authenticate_user, create_access_token, get_password_hash
from repositories.user_repo import add_user

# Load the .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

user_router = APIRouter(
    prefix="/user",
    tags=["User"],
)

@user_router.post("/signup")
async def signup(user: UserSignUpVM):
    hashed_password = get_password_hash(user.Password)
    add_user_dto = AddUserDTO(user.Email, user.Username, hashed_password, user.Role)
    try:
        add_user(add_user_dto)
    except:
        raise HTTPException(status_code=400, detail="This username already exists")
    return JSONResponse(status_code=200, content={"message": "User created successfully"})

@user_router.post("/signin")
async def signin(user: UserSignInVM):
    authenticated_user = authenticate_user(user.Email, user.Password)
    if authenticated_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_data_dict = map_user_to_dict(authenticated_user)
    token = create_access_token(data=user_data_dict)
    return JSONResponse(status_code=200, content={"access_token": token, "token_type": "bearer"})

