import logging
import sys

from multiprocessing import freeze_support
from ufs_tools.python_app_utils.base import AppBase


def main():
    # logging.basicConfig(level=logging.DEBUG)
    AppBase().add_default_module_path()
    from djangoautoconf import DjangoAutoConf
    DjangoAutoConf.set_settings_env()
    # The following is required for freeze app for django
    freeze_support()
    DjangoAutoConf.exe()


if __name__ == "__main__":
    main()
