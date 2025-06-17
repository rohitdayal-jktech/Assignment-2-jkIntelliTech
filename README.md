# ✅ ToDo List API - FastAPI + MySQL

This is a simple **ToDo List REST API** built using **FastAPI**, **MySQL**, and **SQLAlchemy**, with data validation via **Pydantic**.

---

## 📁 Folder Structure

.
├── app/
│ ├── init.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── crud.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── .env
├── .env.example
├── requirements.txt
├── .gitignore
└── README.md


---

## 🚀 Features

- Create, Read, Update, Delete ToDo items
- MySQL backend
- SQLAlchemy ORM
- Pydantic models
- Modular file structure
- Environment variable support using `.env`
- Dockerized using Docker and Docker Compose

---

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- MySQL (via PyMySQL)
- SQLAlchemy
- Pydantic
- Uvicorn
- Docker, Docker Compose
- python-dotenv

---

## ⚙️ Setup Instructions
Dockerized (Recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/rohitdayal-jktech/Assignment-2-jkIntelliTech.git
cd Assignment-2-jkIntelliTech

docker-compose up --build

 