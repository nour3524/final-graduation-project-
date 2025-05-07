from typing import List, Optional
from fastapi import Form, Security, File, UploadFile
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
import uvicorn
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from common import map_object
from models import FaceActivityLog
from repositories import faceLogs_repo
from fastapi.encoders import jsonable_encoder

security = HTTPBearer()

face_logs_router = APIRouter(
    prefix="/face",
    tags=["Face Activity"]
)

@face_logs_router.get("/logs")
async def fetch_face_logs(token: HTTPAuthorizationCredentials = Security(security)):
    logs = faceLogs_repo.get_face_activity_logs()
    response_content = jsonable_encoder([log.__dict__ for log in logs])  # jsonable_encoder handles datetime
    return JSONResponse(status_code=200, content={"logs": response_content})