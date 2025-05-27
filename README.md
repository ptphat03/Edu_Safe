## Edu_Safe

## Clone repository

```bash
git clone https://github.com/ptphat03/Edu_Safe.git
````

```bash
cd Edu_Safe
```

## Kích hoạt môi trường ảo (virtual environment)

Nếu dùng Command Prompt (cmd):

```bash
venv\Scripts\activate.bat
```

Nếu dùng PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

## Chạy backend

```bash
cd backend
uvicorn app.main:app --reload
```

## Chạy frontend

```bash
cd frontend
npm start
```

## Chạy cả backend và frontend cùng lúc

```bash
cd Edu_Safe
npm run dev
```

---

## Ghi chú

* Backend sử dụng FastAPI, chạy bằng `uvicorn`.
* Frontend sử dụng Node.js, chạy bằng `npm start`.
* `npm run dev` được cấu hình để chạy đồng thời backend và frontend (thường dùng package như `concurrently` hoặc tương tự).

---
---

Bạn có muốn mình giúp thêm phần hướng dẫn setup cụ thể hoặc giải thích thêm phần nào không?
```
