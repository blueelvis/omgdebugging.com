+++
title = "NGINX + Apache + LetsEncrypt + WordPress on Ubuntu 18.04 LTS"
description = ""
date = 2019-08-10T11:06:15
updated = 2019-08-10T11:40:47
draft = true
slug = "nginx-apache-letsencrypt"
aliases = ['2019/08/10/nginx-apache-letsencrypt/']
authors = ['Pranav V Jituri']
in_search_index = true
[taxonomies]
tags = []
+++


Recently, I had the opportunity to setup NGINX as the reverse proxy and then
Apache behind it and secure the website with certificates from Let's Encrypt.
The SSL was supposed to terminate at NGINX. The workload behind all of this was
supposed to be WordPress.

This post talks more about the configuration aspect rather than installation of
stuff. You can use the following guides to do the initial setup -

 * Setup WordPress on LAMP Stack
   [https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-lamp-on-ubuntu-18-04#step-1-%E2%80%93-creating-a-mysql-database-and-user-for-wordpress]
 * 

I always create separate users (without sudo privileges) for the websites as
they provide the best isolation.

To create the wordpress site, create a new user using the adduser command, set
its password, log in to the user and then create a new folder say website.com in
the home directory of the user.
Now, login to the user having the permission to interact with Apache and then
create a new file at /etc/apache2/sites-available folder with the following
content -

<VirtualHost *:1111>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.

        ServerName <WEBSITE_URL>

        ServerAdmin webmaster@localhost
        DocumentRoot <FOLDER_PATH_CREATED_ABOVE>

        <Directory <FOLDER_PATH_CREATED_ABOVE> >
                AllowOverride All
                Require all granted
        </Directory>

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog /var/log/<WEBSITE_URL>.error.log
        CustomLog /var/log/<WEBSITE_URL>.access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet


We are going to use Virtual Hosts in Apache for this.

Now, enable Rewrite module - sudo a2enmod rewrite