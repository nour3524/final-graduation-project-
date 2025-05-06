from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ROOT: str = "/api/v1"
    APP_NAME: str = "Insider Lens"
    APP_DESCRIPTION: str = "UEBA"
    DOMAIN: str = "localhost"
    BACKEND_PORT: int = 8080
    DEBUG_MODE: bool = True

settings = Settings()