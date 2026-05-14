from controllers import BaseController
from pathlib import Path


class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str) -> Path:
        project_dir = self.files_dir / project_id
        project_dir.mkdir(parents=True, exist_ok=True)

        return project_dir
