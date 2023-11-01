from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas
from database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

SECRET_KEY = "1234567890"
ALGORITHM = "HS256"
EXPIRATION_TIME = 60 * 60 * 24 * 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def create_access_token(data : dict) :
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes = EXPIRATION_TIME)
    to_encode.update({ "exp" : expire_time })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def verify_access_token(token : str, credentials_exception) :
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        id = payload.get('id')
        if not id :
            raise credentials_exception
        token_data = schemas.TokenData(id = payload.get("id"), role = payload.get("role"), phone = payload.get("phone"), name = payload.get("name"), 
                                       email = payload.get("email"))
    except JWTError :
        raise credentials_exception
    return token_data
    
def get_current_user(token : str = Depends(oauth2_scheme), db : Session = Depends(get_db)) :
    credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, 
                                          detail = "Could not authenticate user",
                                          headers = { "WWW-authenticate" : "Bearer"}
                                          )
    token_data = verify_access_token(token, credentials_exception)
    
    return token_data