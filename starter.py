import logging
import os
from ufs_tools.libtool import include_all

from iconizer.django_in_iconizer.postgresql_checker import PostgreSqlChecker
from iconizer.iconizer_app_root_v2 import IconizerAppRootV2
from iconizer.iconizer_task_config import IconizerTaskConfig

include_all(__file__, "server_base_packages")


__author__ = 'weijia'

log = logging.getLogger(__name__)

os.environ["POSTGRESQL_ROOT"] = "others/pgsql"
# os.environ["UFS_DATABASE"] = "sqlite"


# noinspection PyMethodMayBeStatic
class UfsStarterConfig(IconizerTaskConfig):
    def get_cleanup_task_descriptors(self):
        return [{"stop_postgresql": ["scripts\\postgresql_stop.bat"]}]

    def get_frontend_task_descriptor(self):
        return {"postgresql": ["scripts\\postgresql.bat"]}

    def get_background_tasks(self):
        return (
            self.django_server.get_task_descriptor("git_pull_all"),
            self.django_server.get_task_descriptor("export_evernote"),
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
