from datetime import datetime
from sqlalchemy.orm import Session
from models import SystemReport
from database import ReportModel

def save_report(db: Session, report: SystemReport):
    # Step 1: Add new report
    new_report = ReportModel(
        machine_id=report.machine_id,
        platform=report.platform,
        disk_encryption=report.disk_encryption,
        os_update_status=report.os_update_status,
        antivirus_status=report.antivirus_status,
        sleep_setting_status=report.sleep_setting_status,
        login_check=report.login_check,
        timestamp=report.timestamp or datetime.utcnow()
    )

    db.add(new_report)
    db.commit()

    # Step 2: Keep only latest 10 records per machine_id
    old_reports = (
        db.query(ReportModel)
        .filter(ReportModel.machine_id == report.machine_id)
        .order_by(ReportModel.timestamp.desc())  # Newest first
        .offset(10)  # Skip latest 10
        .all()
    )

    for old_report in old_reports:
        db.delete(old_report)

    db.commit()

def get_all_reports(db: Session) -> list[SystemReport]:
    return db.query(SystemReport).order_by(SystemReport.timestamp.desc()).all()

def get_reports_by_platform(db: Session, platform: str) -> list[SystemReport]:
    return db.query(SystemReport).filter(
        SystemReport.platform.ilike(f"%{platform}%")
    ).order_by(SystemReport.timestamp.desc()).all()
