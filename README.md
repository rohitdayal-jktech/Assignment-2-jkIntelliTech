### ✅ ToDo List API - FastAPI + MySQL

A simple ToDo List REST API built with FastAPI, MySQL, SQLAlchemy, and JWT authentication, using Pydantic for data validation.

---

### 📁 Folder Structure

```plaintext
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
├── .env
├── .env.example
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

### 🚀 Features

- User registration and login with JWT authentication  
- Create, read, update, delete ToDo items  
- MySQL backend with `tododb` database  
- SQLAlchemy ORM for database operations  
- Pydantic models for validation  
- Environment variables via `.env`  
- Dockerized with Docker Compose  
- Local development support  

---

### 🛠️ Tech Stack

- Python 3.12  
- FastAPI  
- MySQL (via PyMySQL)  
- SQLAlchemy  
- Pydantic  
- Uvicorn  
- PyJWT  
- `passlib[bcrypt]`  
- `python-dotenv`  
- Docker, Docker Compose  

---

### ⚙️ Setup Instructions

#### 🚢 Dockerized Deployment

1. **Install Docker and Docker Compose**:
   ```bash
   sudo apt update
   sudo apt install -y docker.io docker-compose
   sudo usermod -aG docker $USER
   newgrp docker
   ```

2. **Create `.env` File**:  
   Copy `.env.example` to `.env` and edit values:

   ```dotenv
   MYSQL_ROOT_PASSWORD=RootPassword123
   MYSQL_DATABASE=tododb
   MYSQL_USER=todo_user
   MYSQL_PASSWORD=TodoPassword123
   DATABASE_URL=mysql+pymysql://todo_user:TodoPassword123@db:3306/tododb
   JWT_SECRET_KEY=<run `openssl rand -hex 32`>
   JWT_ALGORITHM=HS256
   JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

3. **Run Containers**:
   ```bash
   docker-compose up --build
   ```

   Access Swagger docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Stop Containers**:
   ```bash
   docker-compose down
   ```

---

### 📚 API Endpoints

| Method | Endpoint         | Description                | Auth Required |
|--------|------------------|----------------------------|----------------|
| GET    | `/`              | Welcome message            | ❌             |
| POST   | `/register`      | Register user              | ❌             |
| POST   | `/login`         | Get JWT token              | ❌             |
| POST   | `/todos/`        | Create ToDo                | ✅             |
| GET    | `/todos/`        | List ToDos                 | ✅             |
| GET    | `/todos/{id}`    | Get ToDo by ID             | ✅             |
| PUT    | `/todos/{id}`    | Update ToDo                | ✅             |
| DELETE | `/todos/{id}`    | Delete ToDo                | ✅             |

Test with `curl` or Swagger UI at `/docs`.
