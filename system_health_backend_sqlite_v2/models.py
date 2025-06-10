from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SystemReport(BaseModel):
    machine_id: str
    platform: str
    disk_encryption: str
    os_update_status: str
    antivirus_status: str
    sleep_setting_status: str
    login_check:str
    timestamp: Optional[datetime] = None

