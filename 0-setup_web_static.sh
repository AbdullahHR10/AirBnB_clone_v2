#!/usr/bin/env bash
# Sets up your servers for the deployment of web_static

# Installs Nginx if it not already installed
apt update
nginx -v
apt install nginx -y

# Creates the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Creates a fake HTML file /data/web_static/releases/test/index.html to test Nginx configuration
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group.
chown -R ubuntu:ubuntu /data/

# Updates the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to restart Nginx after updating the configuration:
# ...Uses alias inside Nginx configuration
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
service nginx restart
