# lfs-cms
A light, file-based cms that runs on Python

How to get started (Ubuntu/Apache):
1. install apache2
2. install python3 (be sure /usr/bin/python3 exists!)
3. cd into /var/www
4. git clone -b dev https://...
5. a2enmod cgi cgid
6. nano /etc/apache2/sites-enabled/000-default.conf
7. dev v-host setup:
```
<VirtualHost *:80>
    ServerName localhost
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/lfs-cms
    <Directory />
        Options FollowSymLinks
        AllowOverride none
    </Directory>
    ScriptAlias /cgi-bin/ /var/www/lfs-cms/cgi-bin/
    <Directory /var/www/lfs-cms/cgi-bin>
        Options +ExecCGI
        AddHandler cgi-script .cgi .py
        Order allow,deny
        Allow from all
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
8. ufw allow Apache
9. service apache2 restart
10. chmod all scripts in /cgi-bin to +x
11. chmod 762 /var/www/lfs-cms/output.txt
12. go to localhost/public/admin in browser

Ubuntu/Nginx coming soon...
