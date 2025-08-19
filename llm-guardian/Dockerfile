FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update 
RUN apt-get install -y curl
RUN pip install --upgrade pip setuptools wheel

# Copy application code
COPY app/ ./app/
COPY data/ ./data/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser


# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD [ "python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]