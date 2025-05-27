from pydantic import BaseModel
from datetime import date

# ----------------User---------------------
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    username: str
    password: str


    class Config:
        from_attributes = True

