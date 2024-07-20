import jwt 
from fastapi import Header , HTTPException
from dotenv import load_dotenv
load_dotenv()
from config.db import cl 
from bson import ObjectId
import os
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def get_current_user(token: str = Header(...)): 
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = cl.find_one({"_id": ObjectId(user_id)})  
        if user is None:
            raise HTTPException(status_code=401, detail="User not found with this token")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")