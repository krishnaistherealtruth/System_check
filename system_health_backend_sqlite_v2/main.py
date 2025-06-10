from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, ReportModel
from models import SystemReport
from crud import save_report, get_all_reports, filter_reports_by_platform
import pandas as pd
from fastapi.responses import StreamingResponse
import io
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/report")
def receive_report(report: SystemReport, db: Session = Depends(get_db)):
    save_report(db, report)
    return {"message": "Report saved"}

@app.get("/machines")
def list_all_machines(db: Session = Depends(get_db)):
    return get_all_reports(db)

@app.get("/machines/filter")
def filter_by_platform(platform: str, db: Session = Depends(get_db)):
    return filter_reports_by_platform(db, platform)

from fastapi.responses import HTMLResponse



@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h2>System Health Backend is Running</h2><p>Visit <a href='/docs'>/docs</a> for API docs.</p>"


@app.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):
    reports = get_all_reports(db)
    data = [
        {
            "machine_id": r.machine_id,
            "platform": r.platform,
            "disk_encryption": r.disk_encryption,
            "os_update_status": r.os_update_status,
            "antivirus_status": r.antivirus_status,
            "sleep_setting_status": r.sleep_setting_status,
            "login_check":r.login_check,
            "timestamp": r.timestamp,
        }
        for r in reports
    ]

    df = pd.DataFrame(data)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)

    return StreamingResponse(stream, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=system_reports.csv"
    })


@app.get("/report")
def get_reports(db: Session = Depends(get_db)):
    return db.query(ReportModel).all()


