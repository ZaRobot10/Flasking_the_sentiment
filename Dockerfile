# Use an official Python 3.11-slim image as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy your application code and model file to the container
COPY . .

# Expose a port (this is optional since Render will manage $PORT, but it's good practice)
EXPOSE 5001

# Define environment variable for production
ENV FLASK_ENV=production

# Use the shell form to allow environment variable substitution
CMD gunicorn -b 0.0.0.0:$PORT app:app
