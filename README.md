# Edu_Safe

# Clone dự án
git clone https://github.com/ptphat03/Edu_Safe.git

cd Edu_Safe

# Cài backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# (Trong tab khác) Chạy frontend
cd ../frontend
npm install
npm start
