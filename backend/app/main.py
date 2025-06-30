from fastapi import FastAPI
from app.config import settings
from app.db.database import connect_to_db, disconnect_from_db

app = FastAPI(title=settings.app_name, debug=settings.app_debug)

@app.on_event("startup")
async def startup():
    await connect_to_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_from_db()

@app.get("/")
async def read_root():
    return {
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "default_language": settings.default_language,
        "supported_languages": settings.supported_languages.split(",")
    }

@app.get("/languages")
async def get_languages():
    return {
        "default": settings.default_language,
        "supported": settings.supported_languages.split(",")
    }

