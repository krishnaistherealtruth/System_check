from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SystemReport(BaseModel):
    """Pydantic model for incoming system reports"""
    machine_id: str = Field(..., description="Unique identifier for the machine")
    platform: str = Field(..., description="Operating system platform")
    disk_encryption: str = Field(..., description="Disk encryption status")
    os_update_status: str = Field(..., description="OS update status")
    antivirus_status: str = Field(..., description="Antivirus software status")
    sleep_setting_status: str = Field(..., description="Sleep setting configuration status")
    login_check: str =Field(..., description="Password login status")


class SystemReportResponse(SystemReport):
    """Pydantic model for outgoing system reports (includes timestamp)"""
    timestamp: datetime

    class Config:
        from_attributes = True