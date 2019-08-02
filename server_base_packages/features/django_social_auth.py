from djangoautoconf.local_key_manager import ConfigurableAttributeGetter

INSTALLED_APPS += (
    'bootstrapform',
    'userenabootstrap',
    'easy_thumbnails',
    'userena',
    'social.apps.django_app.default',
    'guardian',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    'social.backends.github.GithubOAuth2',
    'guardian.backends.ObjectPermissionBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    # "allauth.account.auth_backends.AuthenticationBackend",
    # 'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    # 'social_auth.backends.contrib.disqus.DisqusBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.orkut.OrkutBackend',
    # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.contrib.vk.VKOAuth2Backend',
    # 'social_auth.backends.contrib.live.LiveBackend',
    # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
    # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    # 'social_auth.backends.contrib.readability.ReadabilityBackend',
    # 'social_auth.backends.contrib.fedora.FedoraBackend',
    # 'social_auth.backends.OpenIDBackend',
    # 'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.contrib.weibo.WeiboBackend',
    'social_auth.backends.contrib.douban.DoubanBackend2',
    'social_auth.backends.contrib.baidu.BaiduBackend',
)

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
LINKEDIN_CONSUMER_KEY = ''
LINKEDIN_CONSUMER_SECRET = ''
ORKUT_CONSUMER_KEY = ''
ORKUT_CONSUMER_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
FOURSQUARE_CONSUMER_KEY = ''
FOURSQUARE_CONSUMER_SECRET = ''
VK_APP_ID = ''
VK_API_SECRET = ''
LIVE_CLIENT_ID = ''
LIVE_CLIENT_SECRET = ''
SKYROCK_CONSUMER_KEY = ''
SKYROCK_CONSUMER_SECRET = ''
YAHOO_CONSUMER_KEY = ''
YAHOO_CONSUMER_SECRET = ''
READABILITY_CONSUMER_SECRET = ''
READABILITY_CONSUMER_SECRET = ''
WEIBO_CLIENT_KEY = ''
WEIBO_CLIENT_SECRET = ''

# LOGIN_URL          = '/login-form/'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/obj_sys/manager/'
LOGIN_ERROR_URL = '/login-error/'

getter = ConfigurableAttributeGetter("weibo_api_keys", "webmanager")
weibo_api_key = getter.get_attr("weibo_api_key")
weibo_api_secret = getter.get_attr("weibo_api_secret")
SOCIAL_AUTH_WEIBO_KEY = weibo_api_key
SOCIAL_AUTH_WEIBO_SECRET = weibo_api_secret
SOCIAL_AUTH_WEIBO_DOMAIN_AS_USERNAME = True

getter = ConfigurableAttributeGetter("qq_api_keys", "webmanager")
qq_api_key = getter.get_attr("qq_api_key")
qq_api_secret = getter.get_attr("qq_api_secret")
SOCIAL_AUTH_QQ_KEY = qq_api_key
SOCIAL_AUTH_QQ_SECRET = qq_api_secret

getter = ConfigurableAttributeGetter("github_api_key", "webmanager")
github_api_key = getter.get_attr("github_api_key")
github_api_secret = getter.get_attr("github_api_secret")
SOCIAL_AUTH_GITHUB_KEY = github_api_key
SOCIAL_AUTH_GITHUB_SECRET = github_api_secret
