import threading
import subprocess
import time
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import HTTPBearer
from fastapi.openapi.utils import get_openapi
from routes import dashboard_router, user_router, face_logs_router, employee_router, analyst_router
from config import settings
from models import ExceptionHandler


app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=settings.APP_NAME,
        version="1.0.0",
        description=settings.APP_DESCRIPTION,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root():
    return """
    <h2 style="text-align:center">
        Click
        <a href="/docs">API DOC</a>
        to see the API doc
    </h2>
    """


# Include your routers
app.include_router(dashboard_router, prefix=settings.APP_ROOT)
# app.include_router(book_router, prefix=settings.APP_ROOT)
app.include_router(user_router, prefix=settings.APP_ROOT)
app.include_router(face_logs_router, prefix=settings.APP_ROOT)
app.include_router(employee_router, prefix=settings.APP_ROOT)   
app.include_router(analyst_router, prefix=settings.APP_ROOT)


@app.exception_handler(ExceptionHandler)
async def handle_exception(_, exc: ExceptionHandler):
    return JSONResponse(
        status_code=exc.status,
        content={"message": f"Oops! {exc.message}, Please try again!"},
    )

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return HTMLResponse("""
    <h2 style="text-align:center">
        Page Not Found
        <br />
        Click
        <a href="/docs">API DOC</a>
        to see the API doc
    </h2>
    """)

app.mount("/static", StaticFiles(directory="static"), name="static")


def run_detection():
    subprocess.run(["python", "api/src/services/detection.py"])

def run_os_collector():
    subprocess.run(["python", "api/src/services/os_collector.py"])

def run_network_collector():
    subprocess.run(["python", "api/src/services/network_collector.py"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEBUG_MODE,
    )
    
#     try:
#         print("🧠 Starting Detection Server...")
#         detection_thread = threading.Thread(target=run_detection)
#         detection_thread.start()

#         print("⏳ Waiting 5 seconds for detection server to be ready...")
#         time.sleep(5)

#         print("🛰️ Starting OS and Network Collectors...")
#         os_thread = threading.Thread(target=run_os_collector)
#         net_thread = threading.Thread(target=run_network_collector)

#         os_thread.start()
#         net_thread.start()

#         os_thread.join()
#         net_thread.join()
#         detection_thread.join()

#     except KeyboardInterrupt:
#         print("\n🛑 Graceful shutdown requested. Exiting...")

    
    
    
