from fastapi import APIRouter
import os

base_router = APIRouter(prefix="/api/v1", tags=["api-v1"])


@base_router.get("/")
def welcome():
    app_name = os.getenv("APP_NAME", "mini-RAG")
    app_version = os.getenv("APP_VERSION","0.1")
    return {"app name ": app_name, "app version": app_version}
