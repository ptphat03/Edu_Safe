from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum

class RoleEnum(str, enum.Enum):
    teacher = "teacher"
    student = "student"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(RoleEnum))

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('users.id'))

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    class_id = Column(Integer, ForeignKey('classes.id'))

class Attendance(Base):
    __tablename__ = "attendances"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    date = Column(Date)
    status = Column(String)  # present / absent
