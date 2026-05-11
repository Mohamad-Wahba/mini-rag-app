from typing import Annotated
from fastapi import APIRouter, Depends
from helpers import get_settings, Settings

base_router = APIRouter(prefix="/api/v1", tags=["api-v1"])
SettingsDep = Annotated[Settings, Depends(get_settings)]


@base_router.get("/")
async def welcome(app_settings: SettingsDep):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"app name ": app_name, "app version": app_version}
