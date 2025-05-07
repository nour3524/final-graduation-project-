from typing import List, Optional
from fastapi import Form, Security, File, UploadFile
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
import uvicorn
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from common import map_object
from models import MaliciousLog
from repositories import dashboard_repo

security = HTTPBearer()

dashboard_router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@dashboard_router.get("/malicious-logs")
async def MaliciousLogs(token: HTTPAuthorizationCredentials = Security(security)):
    try:
        # Fetch malicious logs
        logs = dashboard_repo.get_malicious_logs()

        # Use jsonable_encoder to handle datetime serialization
        response_content = jsonable_encoder([{
            "id": log.LogID,
            "timestamp": log.Timestamp,
            "log_type": log.LogType,
            "details": log.Details,
            "classification": log.Classification
        } for log in logs])

        return JSONResponse(status_code=200, content={"logs": response_content})
    
    except Exception as e:
        # Log the full exception (for debugging purposes)
        import traceback
        traceback.print_exc()

        # Return a clear error message
        return JSONResponse(status_code=500, content={"error": f"Internal Server Error: {str(e)}"})
