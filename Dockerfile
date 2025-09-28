# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /app/

# Expose streamlit port
EXPOSE 8501

# Streamlit runs
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
