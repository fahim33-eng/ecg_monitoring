from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel) :
    name : str
    email : EmailStr
    phone : str
    password : str
    
class UpdateUser(BaseModel) :
    name : str
    phone : str
    password : str
        
class ResponseUser(BaseModel) :
    id : int
    role : int
    name : str
    phone : str
    email : str

    class Config :
        orm_mode = True
        
class UserLogin(BaseModel) :
    email : EmailStr
    password : str

class Token(BaseModel) :
    access_token : str
    token_type : str

class TokenData(BaseModel) :
    id : int | None = None
    role : int | None = None
    phone : str | None = None
    name : str | None = None
    email : str | None = None