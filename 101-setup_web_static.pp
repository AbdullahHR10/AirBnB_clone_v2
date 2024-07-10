# init.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define directories and ownership
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
<head>
<title>Test Page</title>
</head>
<body>
<h1>This is a test page for Nginx configuration</h1>
</body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test/index.html'],
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    location /hbnb_static {
        alias /data/web_static/current;
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}

