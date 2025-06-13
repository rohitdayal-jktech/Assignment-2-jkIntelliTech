from fastapi import FastAPI
from . import models, database, routes

app = FastAPI(title="ToDo List API with MySQL")

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Add routes
app.include_router(routes.router)
