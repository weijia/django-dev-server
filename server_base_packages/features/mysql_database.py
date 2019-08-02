import logging
try:
    from mysql_keys import username, password
except ImportError:
    username = "root"
    password = ""

MYSQL_DATABASE_NAME = "django_apps"

logging.warn("Using mysql database")

if "DATABASES" in locals():
    DATABASES = {}

DATABASES.update({
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': MYSQL_DATABASE_NAME,                # Or path to database file if using sqlite3.
        'USER': username,                      # Not used with sqlite3.
        'PASSWORD': password,                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
})