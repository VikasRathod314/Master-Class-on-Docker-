# Use an official lightweight Python image
FROM python:3.10-slim

# Set/Create working directory
WORKDIR /app

# Copy requirements first (Docker caching best practice)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
