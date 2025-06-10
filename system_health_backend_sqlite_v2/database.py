from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

DATABASE_URL = "sqlite:///./reports_rebuilt.db"

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Database model
class ReportModel(Base):
    __tablename__ = "system_reports"

    machine_id = Column(String, primary_key=True, index=True)
    platform = Column(String, nullable=False)
    disk_encryption = Column(String, nullable=False)
    os_update_status = Column(String, nullable=False)
    antivirus_status = Column(String, nullable=False)
    sleep_setting_status = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)


# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()