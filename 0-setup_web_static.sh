#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Installs Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Creates the folders needed if they don’t already exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

# Creates a fake index.html file with simple content to test Nginx configuration
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>This is a test page for Nginx configuration</h1>
  </body>
</html>" > /data/web_static/releases/test/index.html

# Creates a symbolic link, if it already exists it will be deleted and recreated
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Updates the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restarts Nginx
sudo service nginx restart
