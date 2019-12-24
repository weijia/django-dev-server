CACHES = {
    'default': {
        'BACKEND': 'django_tools.cache.smooth_cache_backends.SmoothFileBasedCache',
        'LOCATION': '/tmp/django_cache',
        'TIMEOUT': 3600  # current value is only a example, it should be a very long time ;)
    },
}
CACHE_MIDDLEWARE_SECONDS = 3600  # current value is only a example, it should be a very long time ;)
LOCAL_SYNC_CACHE_BACKEND = "default"
