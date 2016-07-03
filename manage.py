import logging
import sys

from ufs_tools.libtool import include_all

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)
    try:
        include_all(__file__, "server_base_packages")
    except:
        pass
    from djangoautoconf import DjangoAutoConf
    DjangoAutoConf.set_settings_env()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
