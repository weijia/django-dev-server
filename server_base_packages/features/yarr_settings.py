INSTALLED_APPS += (
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    #'south',
    #'pagination',
    #'webmanager',
    #'tagging',
    #'djangodblog',
    #'registration',
    #'registration_defaults',
    #'django.contrib.staticfiles',
    'yarr',
    'feed_notifier',
    #'template_shortcuts',
    'bootstrap_pagination',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.request",
    "django.core.context_processors.static",
)

ACCOUNT_ACTIVATION_DAYS = 3

LOGIN_REDIRECT_URL = '/yarr/'

#EMAIL_BCMS_QNAME = bae_secrets.bcm_q_name

MIDDLEWARE_CLASSES += (
    'django.middleware.locale.LocaleMiddleware',
    #'pagination.middleware.PaginationMiddleware',
)

ANONYMOUS_USER_ID = -1

SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125

# EMAIL_BACKEND = 'backends.mail_backend.EmailBackend'

ACTIVATION_EMAIL_TEMPLATE = 'registration/activation_email.html'

TEMPLATE_CDN_PROVIDER = "template_shortcuts.providers.sina.Sina"

YARR_MINIMUM_INTERVAL = 1

YARR_FREQUENCY = 10

#DEBUG = False
