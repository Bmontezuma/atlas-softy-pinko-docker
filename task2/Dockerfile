# Use the latest ubuntu image as base
FROM ubuntu:latest

# Update APT repositories and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask

# Set the working directory
WORKDIR /app

# Copy the api.py file into the container
COPY api.py /app/api.py

# Expose port 5252
EXPOSE 5252

# Command to run the Flask server
CMD ["python3", "-u", "api.py"]

