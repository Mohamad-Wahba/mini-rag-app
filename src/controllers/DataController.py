from controllers import BaseController
from fastapi import UploadFile
from models import ResponseSignal


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.scale = 1048576  # 10MB in Bytes

    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPE:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > (self.app_settings.FILE_MAX_SIZE * self.scale):
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
