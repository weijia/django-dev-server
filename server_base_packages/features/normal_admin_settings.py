__author__ = 'weijia'


INSTALLED_APPS += (
    "normal_admin",
)


AUTHENTICATION_BACKENDS += (
    'normal_admin.normal_admin_backend.NormalAdminBackend',
)