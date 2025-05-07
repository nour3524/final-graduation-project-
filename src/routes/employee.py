import uvicorn
from fastapi import APIRouter, Security
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
import os
from common import map_user_to_dict
from repositories.employee_repo import get_employee_records
from models import Employee

security = HTTPBearer()

employee_router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

@employee_router.get("/records")
async def fetch_employee_records():
    try:
        records = get_employee_records()
        response_content = [record.__dict__ for record in records]
        return JSONResponse(status_code=200, content=jsonable_encoder({"employees": response_content}))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
