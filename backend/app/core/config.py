import os
from dotenv import load_dotenv
load_dotenv()

# Sử dụng SQLite thay vì PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./attendance_db.sqlite3")

SECRET_KEY = os.getenv("SECRET_KEY", "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
