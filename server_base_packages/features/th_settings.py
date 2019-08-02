INSTALLED_APPS += (
     'formtools',
     'django_js_reverse',
     'django_th',
     'th_rss',
     # uncomment the lines to enable the service you need
     'th_evernote',
     'th_github',
     # 'th_instapush',
     # 'th_pelican',
     # 'th_pocket',
     # 'th_pushbullet',
     # 'th_todoist',
     # 'th_trello',
     # 'th_twitter',
     # 'th_wallabag',
 )

DJANGO_TH = {
    # paginating
    'paginate_by': 5,

    # this permits to avoid "flood" effect when publishing
    # to the target service - when limit is reached
    # the cache is kept until next time
    # set it to 0 to drop that limit
    'publishing_limit': 5,
    # number of process to spawn from multiprocessing.Pool
    'processes': 5,
    'services_wo_cache': ['th_instapush', ],
    # number of tries before disabling a trigger
    # when management commands run each 15min
    # with 4 'tries' this permit to try on 1 hour
    'failed_tries': 2,  # can exceed 99 - when
    # if you want to authorize the fire button for EACH trigger
    'fire': False,
}

TH_SERVICES = (
    # uncomment the lines to enable the service you need
    'th_evernote.my_evernote.ServiceEvernote',
    'th_github.my_github.ServiceGithub',
    # 'th_instapush.my_instapush.ServiceInstapush',
    # 'th_pelican.my_pelican.ServicePelican',
    # 'th_pocket.my_pocket.ServicePocket',
    # 'th_pushbullet.my_pushbullet.ServicePushbullet',
    # 'th_rss.my_rss.ServiceRss',
    # 'th_slack.my_slack.ServiceSlack',
    # 'th_taiga.my_taiga.ServiceTaiga',
    # 'th_todoist.my_todoist.ServiceTodoist',
    # 'th_trello.my_trello.ServiceTrello',
    # 'th_twitter.my_twitter.ServiceTwitter',
    # 'th_wallabag.my_wallabag.ServiceWallabag',
)


TH_EVERNOTE = {
    # get your credential by subscribing to http://dev.evernote.com/
    # for testing purpose set sandbox to True
    # for production purpose set sandbox to False
    'sandbox': False,
    'consumer_key': '<your evernote key>',
    'consumer_secret': '<your evernote secret>',
}


TH_GITHUB = {
    'username': 'weijia',
    'password': '123456rich',
    'consumer_key': 'a046cd08750574764625',
    'consumer_secret': '96d12c638cc2715de4069ffd4b86b148e17ba689'
}


TH_POCKET = {
    # get your credential by subscribing to http://getpocket.com/developer/
    'consumer_key': '<your pocket key>',
}

TH_PUSHBULLET = {
    'client_id': '<your pushbullet key>',
    'client_secret': '<your pushbullet secret>',
}

TH_TODOIST = {
    'client_id': '<your todoist key>',
    'client_secret': '<your todoist secret>',
}

TH_TRELLO = {
    'consumer_key': '<your trello key>',
    'consumer_secret': '<your trello secret>',
}

TH_TWITTER = {
    # get your credential by subscribing to
    # https://dev.twitter.com/
    'consumer_key': '<your twitter key>',
    'consumer_secret': '<your twitter secret>',
}


CACHES = {
    'default':
    {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR + '/cache/',
        'TIMEOUT': 600,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    },
    # Evernote Cache
    'th_evernote':
    {
        'TIMEOUT': 500,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # GitHub
    'th_github':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Pelican
    'th_pelican':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Pocket Cache
    'th_pocket':
    {
        'TIMEOUT': 500,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Pushbullet
    'th_pushbullet':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/5",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # RSS Cache
    'th_rss':
    {
        'TIMEOUT': 500,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/6",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Todoist
    'th_todoist':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/7",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Trello
    'th_trello':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/8",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Twitter Cache
    'th_twitter':
    {
        'TIMEOUT': 500,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/9",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # Wallabag
    'th_wallabag':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/10",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    'redis-cache':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/11",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 5000,
        }
    },
    'django_th':
    {
        'TIMEOUT': 3600,
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/12",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 5000,
        }
    },
}
