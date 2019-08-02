__author__ = 'weijia'


INSTALLED_APPS += (
    'social.apps.django_app.default',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',
    'social.backends.weibo.WeiboOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    "django.contrib.auth.context_processors.auth",
)

SOCIAL_AUTH_WEIBO_KEY = ''
SOCIAL_AUTH_WEIBO_SECRET = ''

SOCIAL_AUTH_WEIBO_DOMAIN_AS_USERNAME = True