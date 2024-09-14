# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, mkvtoolnix, and postgresql-client
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    mkvtoolnix \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Collect static files
# RUN python manage.py collectstatic --noinput

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Command to run the Django application using Gunicorn
CMD ["gunicorn", "video_processing.wsgi:application", "--bind", "0.0.0.0:8000"]
