from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./reports.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ReportModel(Base):
    __tablename__ = "reports"
    machine_id = Column(String, primary_key=True,unique=True , index=True)
    platform = Column(String)
    disk_encryption = Column(String)
    os_update_status = Column(String)
    antivirus_status = Column(String)
    sleep_setting_status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Automatically create tables
Base.metadata.create_all(bind=engine)
