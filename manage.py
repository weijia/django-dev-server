import logging
import sys
import os

from multiprocessing import freeze_support
from ufs_tools.libtool import include_all
from ufs_tools.python_app_utils.base import AppBase
os.environ["POSTGRESQL_ROOT"] = "others/pgsql"

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    AppBase().add_default_module_path()
    from djangoautoconf import DjangoAutoConf
    DjangoAutoConf.set_settings_env()
    # The following is required for freeze app for django
    freeze_support()
    DjangoAutoConf.exe()
