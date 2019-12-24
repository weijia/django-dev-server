INSTALLED_APPS += ("reversion",)

MIDDLEWARE_CLASSES += (
    'reversion.middleware.RevisionMiddleware',
    # Other middleware goes here...
)