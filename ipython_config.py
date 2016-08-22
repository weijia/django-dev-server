import logging
import sys
import os

from ufs_tools import get_folder
from ufs_tools.app_tools import get_executable_folder
from ufs_tools.basic_lib_tool import include
from ufs_tools.libtool import include_all

# logging.basicConfig(level=logging.DEBUG)
try:
    include_all(__file__, "server_base_packages")
except:
    include(get_executable_folder())


from djangoautoconf import DjangoAutoConf

root_folder = get_folder(__file__)

DjangoAutoConf.set_settings_env(root_folder)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from django.conf import settings

# Password to use for web authentication
# c = get_config()
# c.NotebookApp.password = 'sha1:96b6954d678f:630c0a102b0b7e498dfed0b972f1b5ec19719c02'


c = get_config()

# Notebook config
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
# Ref: https://ipython.org/ipython-doc/dev/notebook/public_server.html1
# In [1]: from IPython.lib import passwd
# In [2]: passwd()
# c.NotebookApp.password = u'sha1:bcd259ccf...[your hashed password here]'
c.NotebookApp.password = 'sha1:96b6954d678f:630c0a102b0b7e498dfed0b972f1b5ec19719c02'
# It is a good idea to put it on a known, fixed port
c.NotebookApp.port = 9999

#Added for IPython 4.0
c.ConnectionFileMixin.ip = u'0.0.0.0'