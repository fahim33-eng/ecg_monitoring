from database import Base
from sqlalchemy import Integer, Boolean, String, Column, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base) :
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    role = Column(Integer, nullable=False, default = 1)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    
    patient = relationship("Patient", back_populates="user", uselist=False)
    
class Patient(Base) :
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, nullable=False)
    message = Column(String)
    fall_detection = Column(Boolean)
    urine_detection = Column(Boolean)
    ecg = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="patient")