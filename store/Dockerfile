# Use the official Python image from the Docker Hub
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . /app
# Run app.py when the container launches
CMD  ["python3", "manage.py", "runserver" , "0.0.0:8000"]
