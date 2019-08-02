from djangoautoconf.local_key_manager import ConfigurableAttributeGetter

INSTALLED_APPS += (
    'social.apps.django_app.default',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS += (
    'social.backends.github.GithubOAuth2',
    # 'social.backends.weibo.WeiboOAuth2',
    # 'social.backends.qq.QQOauth2',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

getter = ConfigurableAttributeGetter("github_api_keys", "djangoautoconf.settings_templates")

github_api_key = getter.get_attr("github_api_key")
github_api_secret = getter.get_attr("github_api_secret")
SOCIAL_AUTH_GITHUB_KEY = github_api_key
SOCIAL_AUTH_GITHUB_SECRET = github_api_secret