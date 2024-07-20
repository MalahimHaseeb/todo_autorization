from pydantic import BaseModel , EmailStr


class User(BaseModel):
    name : str
    password : str
    email : EmailStr

class UserResponse(BaseModel):
    name: str
    email: EmailStr

class Password(BaseModel):
     email : EmailStr
     password : str