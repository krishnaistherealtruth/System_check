from datetime import datetime, timezone
from sqlalchemy.orm import Session
from models import SystemReport
from database import ReportModel

def save_report(db: Session, report: SystemReport):
    new_report = ReportModel(
        machine_id=report.machine_id,
        platform=report.platform,
        disk_encryption=report.disk_encryption,
        os_update_status=report.os_update_status,
        antivirus_status=report.antivirus_status,
        sleep_setting_status=report.sleep_setting_status,
        login_check=report.login_check,
        timestamp=report.timestamp or datetime.utcnow()  # ✅ Use incoming or fallback
    )
    existing = db.query(ReportModel).filter_by(machine_id=report.machine_id).first()
    if existing:
        for field, value in report.dict().items():
            setattr(existing, field, value)
        existing.timestamp = report.timestamp or datetime.utcnow()
    else:
        db.add(new_report)

    db.commit()

def get_all_reports(db: Session):
    return db.query(ReportModel).order_by(ReportModel.timestamp.desc()).all()

def get_reports_by_platform(db: Session, platform: str):
    return db.query(ReportModel).filter(
        ReportModel.platform.ilike(f"%{platform}%")
    ).order_by(ReportModel.timestamp.desc()).all()
