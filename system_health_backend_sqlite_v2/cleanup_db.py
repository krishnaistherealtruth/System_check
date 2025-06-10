from database import SessionLocal, ReportModel

def clean_dummy_rows():
    db = SessionLocal()
    deleted = db.query(ReportModel).filter(ReportModel.machine_id == 'string').delete()
    db.commit()
    db.close()
    print(f"Deleted {deleted} invalid record(s).")

if __name__ == "__main__":
    clean_dummy_rows()
