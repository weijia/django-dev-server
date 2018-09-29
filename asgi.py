import os
from channels.asgi import get_channel_layer
from ufs_tools.libtool import include_all

from manage import main


include_all(os.path.dirname(__file__), "server_base_packages")
main()
channel_layer = get_channel_layer()
