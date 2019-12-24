__author__ = 'weijia'
INSTALLED_APPS += ('bootstrap_pagination',)

MIDDLEWARE_CLASSES += (
    #'obj_sys.middleware.XsSharingMiddleware',
    'pagination.middleware.PaginationMiddleware',
)