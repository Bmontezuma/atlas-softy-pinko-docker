# Use the official Ubuntu base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Upgrade installed packages
RUN apt-get upgrade -y

# Install Python 3 and pip3
RUN apt-get install -y python3 python3-pip

# Install Flask and Flask-CORS
RUN pip3 install flask flask-cors

# Set the working directory in the container
WORKDIR /app

# Copy the API script into the container
COPY ./api.py /app/api.py

# Expose port 5252 to the outside world
EXPOSE 5252

# Command to run the Flask application
CMD ["python3", "api.py"]
