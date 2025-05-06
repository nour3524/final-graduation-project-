from fastapi import APIRouter, Security
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from repositories.analyst_repo import get_analyst_records

analyst_router = APIRouter(
    prefix="/analysts",
    tags=["Analysts"]
)

@analyst_router.get("/records")
async def fetch_analyst_records():
    try:
        records = get_analyst_records()
        response_content = [record.__dict__ for record in records]
        return JSONResponse(status_code=200, content=jsonable_encoder({"analysts": response_content}))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})