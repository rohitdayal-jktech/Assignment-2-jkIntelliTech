from fastapi import FastAPI, Request
from . import models, database, routes
import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ToDo List API with MySQL")

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Request: {request.method} {request.url} at {datetime.utcnow()}")
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Completed in {duration:.2f} seconds")
    return response



# Add routes
app.include_router(routes.router)
