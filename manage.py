import logging
import sys

from ufs_tools.libtool import include_all
from ufs_tools.python_app_utils.base import AppBase


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    AppBase().add_default_module_path()
    from djangoautoconf import DjangoAutoConf
    DjangoAutoConf.set_settings_env()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
