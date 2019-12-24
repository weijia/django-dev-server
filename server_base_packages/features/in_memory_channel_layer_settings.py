# In settings.py
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "ROUTING": "djangoautoconf.auto_detection.default_routing.channel_routing",
    },
}
