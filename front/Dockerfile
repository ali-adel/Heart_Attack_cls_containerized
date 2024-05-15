# Use httpd image as base
FROM httpd:alpine

# Copy your HTML file and CSS file to the appropriate directory
COPY index.html /usr/local/apache2/htdocs/
COPY style.css /usr/local/apache2/htdocs/

# Expose port 80 to the outside world
EXPOSE 80