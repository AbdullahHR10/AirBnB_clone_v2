#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Installs Nginx if it not already installed
sudo apt update
sudo apt install nginx

# Creates the folders needed if they don’t already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

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
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Updates the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

# Restarts Nginx
sudo service nginx restart
