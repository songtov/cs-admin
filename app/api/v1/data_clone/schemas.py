from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel

class DataCloneOptions(BaseModel):
    overwrite: bool = False
    exclude_tables: Optional[list[str]] = None
    include_tables: Optional[list[str]] = None

class DataCloneRequest(BaseModel):
    source: str
    target: str
    options: Optional[DataCloneOptions] = None

class DataCloneStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

class DataCloneResponse(BaseModel):
    run_id: str
    status: DataCloneStatus
    conf: Dict
    start_date: Optional[str] = None
    end_date: Optional[str] = None
