import logging
import os
from ufs_tools.libtool import include_all

include_all(__file__, "server_base_packages")

from iconizer.django_in_iconizer.django_in_iconizer import DjangoInIconizer
from iconizer.django_in_iconizer.postgresql_checker import PostgreSqlChecker
from iconizer.iconizer_app_root import IconizerAppRoot


__author__ = 'weijia'

log = logging.getLogger(__name__)

os.environ["POSTGRESQL_ROOT"] = "others/pgsql"
os.environ["UFS_DATABASE"] = "sqlite"


class UfsStarter(IconizerAppRoot):
    # noinspection PyAttributeOutsideInit
    def init_parameters(self):
        super(UfsStarter, self).init_parameters()
        django_server = DjangoInIconizer()
        self.front_end_task = {"postgre_sql": ["scripts\\postgresql.bat"]}
        self.background_tasks = (
                                 # {"web_server": ["manage_with_conf.py", "runserver", "8110"]},
                                 # django_server.get_django_task("create_default_super_user"),
                                 # django_server.get_django_task("migrate"),
                                 # django_server.get_django_task("syncdb", ["--noinput"]),
                                 # django_server.get_django_task("drop_tagger"),
                                 # {"background_tasks": ["manage_with_conf.py", "process_tasks"]},
                                 # {"ipynb": ["manage.py", "shell_ipynb"]},
                                 # {"ipynb": ["jupyter-notebook.exe", "--config=ipython_config.py"]},
                                 # {"clipboard_monitor": ["manage.py", "clipboard_monitor_task"]},
                                 # {"web_server": ["cherrypy_server.py", ]}),
                                 # {"ipynb": ["jupyter-notebook.exe", "--config=ipython_config.py"]})
                                 )

        self.app_root_folder_name = "server_for_django_15_and_below"
        self.cleanup_tasks = [{"stop_postgre_sql": ["scripts\\postgresql_stop.bat"]}]

    def sync_to_main_thread(self):
        p = PostgreSqlChecker()
        p.wait_for_database_ready()
        if not p.is_django_table_created():
            # os.system("python manage_with_conf.py syncdb --noinput")
            os.system("python manage_with_conf.py migrate")
            os.system("python manage_with_conf.py create_default_super_user")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    UfsStarter().start_iconized_applications()
