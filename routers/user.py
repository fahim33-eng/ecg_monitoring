from fastapi import FastAPI, Response, HTTPException, Depends, APIRouter
from fastapi.params import Body
import models
from database import get_db
from sqlalchemy.orm import Session
from schemas import User, ResponseUser, ResponsePatient, Patient
from passlib.context import CryptContext

router = APIRouter()

@router.post("/users", status_code = 201, response_model = ResponseUser, tags=['users'])
def create_user(user : User ,db : Session = Depends(get_db)) :
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_pass = pwd_context.hash(user.password)
    user.password = hashed_pass
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{id}", response_model = ResponseUser, tags=['users'])
def get_user(id : int, db : Session = Depends(get_db)) :
    user = db.query(models.User).filter(models.User.id == id).first()
    return user

@router.delete("/users/{id}", response_model = ResponseUser, tags=['users'])
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user

@router.get("/patients/{id}", response_model = ResponsePatient, tags=['patients'])
def get_patient(id : int, db : Session = Depends(get_db)) :
    patient = db.query(models.Patient).filter(models.Patient.user_id == id).first()
    return patient

@router.post("/patients", status_code = 201, response_model = ResponsePatient, tags=['patients'])
def create_patient(patient : Patient, db : Session = Depends(get_db)) :
    new_patient = models.Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient