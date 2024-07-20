from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel
from object.userobject import User, UserResponse, Password
from config.db import cl, todocl
import bcrypt
import jwt  # Correct import for PyJWT
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

app = FastAPI()
userr = APIRouter()
todor = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

@userr.get("/")
def starting_point():
    return {"message": "Welcome to our todo app"}

@userr.post("/signup", tags=["user-routes"])
def post_user(user: User):
    # Check if email already exists
    existing_user = cl.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_dict = {
        "name": user.name,
        "password": hashed_password.decode('utf-8'),
        "email": user.email
    }
    cl.insert_one(user_dict)
    return {"success": True, "message": "Successfully Signup", "user": UserResponse(name=user.name, email=user.email)}

@userr.post("/login", response_model=Token, tags=["user-routes"])
def password_match(password: Password):
    user = cl.find_one({"email": password.email})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if bcrypt.checkpw(password.password.encode('utf-8'), user["password"].encode('utf-8')):
        print(user)
        encoded = jwt.encode({"user_id": str(user["_id"])}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": encoded, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Incorrect password or email")
