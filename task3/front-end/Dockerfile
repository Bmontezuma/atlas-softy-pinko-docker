# Use the official Nginx base image
FROM nginx:latest

# Copy the static content for the front-end into the container
COPY . /var/www/html/softy-pinko-front-end

# Copy the Nginx configuration file
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
