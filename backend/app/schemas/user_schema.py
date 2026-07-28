from pydantic import BaseModel, EmailStr, Field #type: ignore[reportMissingImports]

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str = Field(min_length=8, max_length=72)

class UserLogin(BaseModel):
    email:EmailStr
    password:str