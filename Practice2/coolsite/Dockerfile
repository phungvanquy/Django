# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /coolsite
WORKDIR /coolsite

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# RUN ["python", "manage.py", "migrate"]

# CMD ["gunicorn", "coolsite.wsgi:application", "--bind", "0.0.0.0:8000"]