from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    teacher = "teacher"
    student = "student"

class UserOut(BaseModel):
    id: int
    username: str
    role: RoleEnum

    class Config:
        from_attributes  = True
