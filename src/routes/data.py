from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile
from helpers import get_settings, Settings
from controllers import DataController

data_router = APIRouter(prefix="/api/v1/data", tags=["api-v1", "data"])
SettingsDep = Annotated[Settings, Depends(get_settings)]


@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, app_settings: SettingsDep):
    is_valid, ResponseSignal = DataController().validate_uploaded_file(file=file)
    return {"valid file?": is_valid, "signal": ResponseSignal}
