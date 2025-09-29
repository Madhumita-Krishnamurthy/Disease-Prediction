# Use a lightweight Python base image
FROM python:3.10-slim

# Prevent Python from writing pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
# On Render, $PORT is injected, so we map Streamlit to it
CMD ["streamlit", "run", "ml.py", "--server.port=$PORT", "--server.address=0.0.0.0"]
