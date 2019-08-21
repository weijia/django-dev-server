import logging

try:
    from mysql_keys import username, password
except ImportError:
    username = "root"
    password = "root"

logging.warn("Using mysql database on /var/lib/mysql/mysql.sock")

if "DATABASES" not in __builtins__:
    DATABASES = []

DATABASES.update({
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_apps',  # Or path to database file if using sqlite3.
        'USER': "4labs_user",  # Not used with sqlite3.
        'PASSWORD': "4labs_password",  # Not used with sqlite3.
        # 'HOST': 'hz4labs02.china.nsn-net.net',             # Set to empty string for localhost. Not used with sqlite3.
        # https://coderwall.com/p/raueiw/mysql-use-unix-socket-in-django-settings
        "OPTIONS": {
            "unix_socket": "/var/lib/mysql/mysql.sock",
        },
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
})
