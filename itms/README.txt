1. Install Python 2.7
2. Install PIP 
    apt-get install python-pip
--------------------------------------------------------------------------------
3. Install mysql 
   apt-get install mysql-server
------------------------------------------------------------------------------
4. pip install django-cms==2.4.3 (Dependencies as follow)
    -- django==1.5.8
    -- django-classy-tags==0.5.2
    -- django-mptt==0.5.2
    -- django-sekizai==0.8.1
    -- html5lib==0.999
    -- six==1.9.0
    -- South==1.0.2
    # Optional, recommended packages
    #-- pil==1.1.7 (To use ImageFields, must install)
    -- django-filter==0.9.1
    #-- cmsplugin-filer==0.10.1

------------------------------------------------------------------------------
5.  pip install mysql-python==1.2.5

------------------------------------------------------------------------------
6.  pip install django-pagination==1.0.7 (page tuning)
------------------------------------------------------------------------------
7.  pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter  # Filtering support
------------------------------------------------------------------------------
8. git clone ssh://xxx@git-ccr-1.devtools.intel.com:29418/imediapro-itms2 itms
-------------------------------------------------------------------------------
9. apt-get install apache2
--------------------------------------------------------------------------------
10. apache config
vim /etc/apache2/sites-available/000-default.conf

<VirtualHost *:80>
       # The ServerName directive sets the request scheme, hostname and port that
       # the server uses to identify itself. This is used when creating
       # redirection URLs. In the context of virtual hosts, the ServerName
       # specifies what hostname must appear in the request's Host: header to
       # match this virtual host. For the default virtual host (this file) this
       # value is not decisive as it is used as a last resort host regardless.
       # However, you must set it for any further virtual host explicitly.
       #ServerName www.example.com
  
        ServerAdmin feix.li@intel.com
        DocumentRoot /home/jason/itms
	    WSGIPassAuthorization On
        ServerName jason-itms.sh.intel.com
  
        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn
        <Directory /home/jason/itms>
                Options FollowSymLinks
                AllowOverride None
                Require all granted
        </Directory>
  
        WSGIScriptAliasMatch (?i)^/ "/home/jason/itms/itms/wsgi.py"
        <Directory "/home/jason/itms/itms/wsgi.py">
                Options Indexes FollowSymLinks ExecCGI
                AllowOverride None
                Require all granted
        </Directory>
 
        Alias /static /home/jason/itms/static/
        <Directory /home/jason/itms/statics>
                Require all granted
        </Directory>
    
        Alias /doc /home/jason/itms/docs/build/html/
        <Directory "/home/jason/itms/docs/build/html">
                Options Indexes
                Allow from all
        </Directory>
   
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

  
		# For most configuration files from conf-available/, which are
		# enabled or disabled at a global level, it is possible to
		# include a line for only one particular virtual host. For example the
		# following line enables the CGI configuration for this host only
		# after  it has been globally disabled with "a2disconf".
		#Include conf-available/serve-cgi-bin.conf
  </VirtualHost>
---------------------------------------------------------------------------------
11.
    cd /home/media/itms/statics
    python ../manager.py collectstatic
---------------------------------------------------------------------------------
