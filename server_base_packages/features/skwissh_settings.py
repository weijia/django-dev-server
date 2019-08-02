INSTALLED_APPS += (
#    'pagination',
'kronos',    
'skwissh',
)

MIDDLEWARE_CLASSES += (
#'django.contrib.auth.middleware.AuthenticationMiddleware',
#'django.contrib.sessions.middleware.SessionMiddleware',
#'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
'django.core.context_processors.i18n',
    'django.core.context_processors.static',
)

LANGUAGES = (
   ('en', 'English'),
)

#MIDDLEWARE_CLASSES += (
#    #'obj_sys.middleware.XsSharingMiddleware',
#    'pagination.middleware.PaginationMiddleware',
#)
