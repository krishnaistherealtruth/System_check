from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SystemReport(BaseModel):
    machine_id: str
    platform: str
    disk_encryption: str
    os_update_status: str
    antivirus_status: str
    sleep_setting_status: str
    login_check: str
    timestamp: Optional[datetime] = None  # Accept client or fallback in crud
