from fastapi import APIRouter, Depends, UploadFile
from helpers.config import get_settings, Settings

data_router = APIRouter(prefix="/api/v1/data", tags=["api-v1", "data"])


@data_router.post("/upload/{project_id}")
async def upload_file(
    project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)
):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "where": "upload_file",
        "project_id": project_id,
        "app name ": app_name,
        "app version": app_version,
        "file type": file.content_type,
        "file name": file.filename,
    }
