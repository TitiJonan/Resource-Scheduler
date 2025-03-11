# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code to the container
COPY resource_scheduler.py /app

# Install required packages
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Command to run the app
CMD ["python", "resource_scheduler.py"]