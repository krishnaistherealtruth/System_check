from sqlalchemy.orm import Session
from models import SystemReport
from datetime import datetime
from database import ReportModel


def save_report(db: Session, report: SystemReport):
    db_report = db.query(ReportModel).filter(ReportModel.machine_id == report.machine_id).first()

    if db_report:
        # Update existing record
        db_report.platform = report.platform
        db_report.disk_encryption = report.disk_encryption
        db_report.os_update_status = report.os_update_status
        db_report.antivirus_status = report.antivirus_status
        db_report.sleep_setting_status = report.sleep_setting_status
        db_report.timestamp = report.timestamp or datetime.utcnow()
    else:
        # Create new record
        db_report = ReportModel(
            machine_id=report.machine_id,
            platform=report.platform,
            disk_encryption=report.disk_encryption,
            os_update_status=report.os_update_status,
            antivirus_status=report.antivirus_status,
            sleep_setting_status=report.sleep_setting_status,
            timestamp=report.timestamp or datetime.utcnow()
        )
        db.add(db_report)

    db.commit()



def get_all_reports(db: Session):
    return db.query(ReportModel).all()

def filter_reports_by_platform(db: Session, platform_name: str):
    return db.query(ReportModel).filter(ReportModel.platform.ilike(platform_name)).all()
