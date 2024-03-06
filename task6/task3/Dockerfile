# Use the latest ubuntu image as base
FROM ubuntu:latest

# Update APT repositories and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask

# Set the working directory for the back-end
WORKDIR /app

# Copy the api.py file into the container
COPY api.py /app/api.py

# Expose port 5252 for the back-end
EXPOSE 5252

# Command to run the Flask server
CMD ["python3", "-u", "api.py"]

# Change working directory for the front-end
WORKDIR /var/www/html/softy-pinko-front-end

# Copy the front-end files into the container
COPY softy-pinko-front-end/ /var/www/html/softy-pinko-front-end

# Copy Nginx configuration file
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf

# Expose port 9000 for the front-end
EXPOSE 9000

