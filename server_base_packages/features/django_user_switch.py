__author__ = 'weijia'


INSTALLED_APPS += (
    'userswitch',
)

MIDDLEWARE_CLASSES += (
  'userswitch.middleware.UserSwitchMiddleware',
)

USERSWITCH_OPTIONS = {
    'css_inline': 'position:absolute;top:200px;right:5px;z-index:16777271;',
}