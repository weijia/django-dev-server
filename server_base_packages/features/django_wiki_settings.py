# coding=utf-8
from django.utils.translation import gettext

# Requirement: pip install wiki

INSTALLED_APPS += (
    'django.contrib.humanize',
    'django_nyt',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',
    # 'blog',
    # 'zinnia',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "sekizai.context_processors.sekizai",
)

# LANGUAGE_CODE = 'zh-CN'
#
# LANGUAGES = (
#     ('zh-CN', u'简体中文'), # instead of 'zh-CN'
# )


# The following is for mayblog instead of wiki. Just keep it.
# MAY_BLOG = {
#     "PER_PAGE": 5,
#     'PER_PAGE_ADMIN': 5,
#     "RSS_NUM": 5,
# }
