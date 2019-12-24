import django

if django.VERSION[1] < 6:
    INSTALLED_APPS += (
        'south',
    )
