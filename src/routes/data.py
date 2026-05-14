from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers import get_settings, Settings
from controllers import DataController

data_router = APIRouter(prefix="/api/v1/data", tags=["api-v1", "data"])
SettingsDep = Annotated[Settings, Depends(get_settings)]


@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, app_settings: SettingsDep):
    is_valid, response_signal = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"signal": response_signal}
        )
