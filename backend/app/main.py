# app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import router
from fastapi.middleware.cors import CORSMiddleware

# Tạo bảng nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
