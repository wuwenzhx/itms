# Django settings for itms project.
import os
import socket
import ldap
from django_auth_ldap.config import *

HOSTNAME = socket.gethostname()
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

ADMINS = (
    ('Li Fei', 'feix.li@intel.com'),
    ('Xu Ying', 'yingx.xu@intel.com'),
    ('Wang Zhaoyu', 'zhaoyux.wang@intel.com'),
)

MANAGERS = ADMINS

if 'itms-server' == HOSTNAME:
    DEBUG = False
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'itms_new',  # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'root',
            'PASSWORD': 'intel123',
            'HOST': '',
            # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '3306',  # Set to empty string for default.
        }
    }
else:
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'spdk_sh',  # Or path to database file if using sqlite3.
            #The following settings are not used with sqlite3:
            'USER': 'root',
            'PASSWORD': '1',
            'HOST': '127.0.0.1',
            # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '3306',  # Set to empty string for default.
        }
    }

TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://corpad.glb.intel.com:3268"
 #AUTH_LDAP_BIND_DN = "cn=TSIE LDAP,ou=DC,ou=MCG TSIE,ou=Resources,dc=ccr,dc=corp,dc=intel,dc=com"
 #AUTH_LDAP_BIND_PASSWORD = "intel123!"
AUTH_LDAP_BIND_DN = "cn=lab_itms_ldap,ou=Generic-Account,ou=Resources,dc=ccr,dc=corp,dc=intel,dc=com"
AUTH_LDAP_BIND_PASSWORD = "intel123$"
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    LDAPSearch("ou=Workers,dc=ccr,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
    LDAPSearch("ou=Workers,dc=amr,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
    LDAPSearch("ou=Workers,dc=gar,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
    LDAPSearch("ou=Workers,dc=ger,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
    LDAPSearch("ou=DC,ou=MCG TSIE,ou=Resources,dc=ccr,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE,
               "(sAMAccountName=%(user)s)"),
    LDAPSearch("ou=Generic-Account,ou=Resources,dc=ccr,dc=corp,dc=intel,dc=com", ldap.SCOPE_SUBTREE,
               "(sAMAccountName=%(user)s)"),
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Rialto,ou=Application Managed,ou=Groups,dc=amr,dc=corp,dc=intel,dc=com",
                                    ldap.SCOPE_SUBTREE)
AUTH_LDAP_GROUP_TYPE = NestedMemberDNGroupType(member_attr='member')

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

AUTH_LDAP_USER_ATTR_MAP = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

AUTH_LDAP_MIRROR_GROUPS = True
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1800

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "statics"),
    os.path.join(PROJECT_PATH, "plugins"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-x$)5q3thkfswhrg-k4py$q-s0l5d5#0%r=vduke$$_j+h95^v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'pagination.middleware.PaginationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'itms.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'itms.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "templates"),
)

CMS_TEMPLATES = (
    ('requirement.html', 'T_Req'),
    ('feature.html', 'T_Feature'),
    ('testcase.html', 'T_TestCase'),
    ('testsuite.html', 'T_TestSuite'),
    ('testplan.html', 'T_TestPlan'),
    ('report.html', 'T_Report'),
    ('regular_report.html', 'T_Regular'),
    ('undated_report.html', 'T_Undated'),
    ('normal.html', 'T_Normal'),
    ('home.html', 'T_Index'),
    ('app.html', 'T_App'),
    ('upload.html', 'T_Upload'),
    ('execution.html', 'T_Exe'),
    ('itec.html', 'T_iTEC'),
    #('nvme_driver.html', 'T_NvmeDriver'),
    ('blank.html', 'T_Blank'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'cms',
    'mptt',
    'menus',
    'south',
    'rest_framework',
    'restapi',
    'sekizai',
    'pagination',
    'base_models',
    #'plugins.casecenter',
    'plugins.report',
    'plugins.index',
    'plugins.upload',
    'plugins.execution',
    'plugins.nvme_driver'
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
