from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

url = "postgresql://postgres:password@localhost/ecg_monitoring"
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()