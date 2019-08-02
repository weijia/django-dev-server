ANONYMOUS_USER_ID = -1

INSTALLED_APPS += (
    'guardian',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)