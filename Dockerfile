# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files including wait-for-it.sh
COPY . .

# Make wait-for-it.sh executable
RUN chmod +x /app/wait-for-it.sh

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Use wait-for-it.sh before starting FastAPI
CMD ["./wait-for-it.sh", "db:3306", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
