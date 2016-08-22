import logging
import os

from ufs_tools.app_tools import get_executable_folder
from ufs_tools.python_app_utils.base import AppBase
from ufs_tools.file_search import find_filename_in_app_folder

AppBase().add_default_module_path()

from iconizer.django_in_iconizer.postgresql_checker import PostgreSqlChecker
from iconizer.iconizer_app_root_v2 import IconizerAppRootV2
from iconizer.iconizer_task_config import IconizerTaskConfig


__author__ = 'weijia'

log = logging.getLogger(__name__)

os.environ["POSTGRESQL_ROOT"] = os.path.join(get_executable_folder(), "others/pgsql")
# os.environ["UFS_DATABASE"] = "sqlite"


# noinspection PyMethodMayBeStatic
class UfsStarterConfig(IconizerTaskConfig):
    def get_cleanup_task_descriptors(self):
        stop_script = find_filename_in_app_folder("postgresql_stop.bat")
        return [{"stop_postgresql": [stop_script]}]

    def get_frontend_task_descriptor(self):
        start_script = find_filename_in_app_folder("postgresql.bat")
        return {"postgresql": [start_script]}

    def get_background_tasks(self):
        return (
            self.django_server.get_run_server_task_descriptor(),
            self.django_server.get_task_descriptor("git_pull_all"),
            self.django_server.get_task_descriptor("cronserver"),
        )

    def sync_to_main_thread(self):
        p = PostgreSqlChecker()
        p.wait_for_database_ready()
        if not p.is_django_table_created():
            self.init_ufs_db()

    def init_ufs_db(self):
        self.django_server.execute_cmd("migrate")
        self.django_server.execute_cmd("create_default_super_user")


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    IconizerAppRootV2(UfsStarterConfig()).start_iconized_applications()
