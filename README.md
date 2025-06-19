✅ ToDo List API - FastAPI + MySQL
A simple ToDo List REST API built with FastAPI, MySQL, SQLAlchemy, and JWT authentication, using Pydantic for data validation.

📁 Folder Structure
Assignment-2-jkIntelliTech/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── test_db.py
│   └── test_env.py
├── .env
├── .env.example
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


🚀 Features

User registration and login with JWT authentication
Create, read, update, delete ToDo items
MySQL backend with tododb database
SQLAlchemy ORM for database operations
Pydantic models for validation
Environment variables via .env
Dockerized with Docker Compose
Local development support


🛠️ Tech Stack

Python 3.12
FastAPI
MySQL (via PyMySQL)
SQLAlchemy
Pydantic
Uvicorn
PyJWT
passlib[bcrypt]
python-dotenv
Docker, Docker Compose


⚙️ Setup Instructions
Dockerized Deployment

Install Docker and Docker Compose:
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker


Create .env File:Copy .env.example to .env and edit:
MYSQL_ROOT_PASSWORD=RootPassword123
MYSQL_DATABASE=tododb
MYSQL_USER=todo_user
MYSQL_PASSWORD=TodoPassword123
DATABASE_URL=mysql+pymysql://todo_user:TodoPassword123@db:3306/tododb
JWT_SECRET_KEY=<run `openssl rand -hex 32`>
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30


Run Containers:
docker-compose up --build

Access at http://localhost:8000/docs.

Stop Containers:
docker-compose down




📚 API Endpoints

GET /: Welcome message
POST /register: Register user ({"username": "testuser", "password": "TestPass123"})
POST /login: Get JWT token (username=testuser&password=TestPass123)
POST /todos/: Create ToDo (requires JWT)
GET /todos/: List ToDos (requires JWT)
GET /todos/{id}: Get ToDo by ID (requires JWT)
PUT /todos/{id}: Update ToDo (requires JWT)
DELETE /todos/{id}: Delete ToDo (requires JWT)

Test with curl or Swagger UI (/docs).



