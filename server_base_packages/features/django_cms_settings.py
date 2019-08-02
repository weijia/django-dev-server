# coding=utf-8
INSTALLED_APPS += (
    'django.contrib.sites',
    'filer',
    'easy_thumbnails',
    'mptt',
    'cms',
    'menus',
    'treebeard',
    'djangocms_text_ckeditor',
)

MIDDLEWARE_CLASSES += (
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)


LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
    ('zh-hans', '简体中文'),
]

TEMPLATES[0]['OPTIONS']['context_processors'].extend([
                'cms.context_processors.cms_settings',
            ])

CMS_TEMPLATES = [
    ('home.html', 'Home page template'),
]
