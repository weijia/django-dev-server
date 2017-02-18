import logging
import os

from ufs_tools import find_callable_in_app_framework
from ufs_tools.app_tools import get_executable_folder
from ufs_tools.python_app_utils.base import AppBase
# from ufs_tools.file_search import find_filename_in_app_folder

AppBase().add_default_module_path()

from iconizer.django_in_iconizer.postgresql_checker import PostgreSqlChecker
from iconizer.iconizer_app_root_v2 import IconizerAppRootV2
from iconizer.iconizer_task_config import IconizerTaskConfig


__author__ = 'weijia'

log = logging.getLogger(__name__)

# os.environ["POSTGRESQL_ROOT"] = os.path.join(get_executable_folder(), "others/pgsql")
# os.environ["UFS_DATABASE"] = "sqlite"


# noinspection PyMethodMayBeStatic
class UfsStarterConfig(IconizerTaskConfig):
    def get_cleanup_task_descriptors(self):
        return []

    def get_frontend_task_descriptor(self):
        return self.django_server.get_task_descriptor("runserver", ["--noreload", "0.0.0.0:8888"])

    def get_background_tasks(self):
        return (
            {"redis": [find_callable_in_app_framework("redis-server")]},
            # self.django_server.get_task_descriptor("git_pull_all"),
            # self.django_server.get_task_descriptor("start_device_management_daemon"),
            self.django_server.get_task_descriptor("cronserver"),
        )

    def start_other_tasks_depends_on_frontend_task(self):
        self.django_server.execute_cmd("migrate")
        self.django_server.execute_cmd("create_default_super_user")


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    IconizerAppRootV2(UfsStarterConfig()).start_iconized_applications()
