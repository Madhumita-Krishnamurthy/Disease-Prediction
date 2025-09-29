# Use lightweight Python image
FROM python:3.10-slim

# Prevents writing pyc files and forces output to terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Start app using Gunicorn
# "ml:app" means -> file `ml.py` contains variable `app = Flask(__name__)`
# If your Flask instance has a different name, adjust this
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "ml:app"]
