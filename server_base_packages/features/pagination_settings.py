INSTALLED_APPS += (
    'pagination',
)

MIDDLEWARE_CLASSES += (
    #'obj_sys.middleware.XsSharingMiddleware',
    'pagination.middleware.PaginationMiddleware',
)
