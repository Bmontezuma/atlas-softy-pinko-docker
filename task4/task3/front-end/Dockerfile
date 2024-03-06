# Base image
FROM nginx:latest

# Copy the front-end files to the Nginx document root
COPY softy-pinko-front-end /var/www/html/softy-pinko-front-end

# Copy Nginx configuration file
COPY softy-pinko-front-end.conf /etc/nginx/conf.d/default.conf
