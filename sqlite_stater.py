import logging

from iconizer.iconizer_app_root import IconizerAppRoot

log = logging.getLogger(__name__)


class UfsStarterWithSqlite(IconizerAppRoot):
    front_end_task = {"web_server": ["manage.py", "runserver", "8110"]}
    background_tasks = ({"drop_tagger": ["manage.py", "drop_tagger"]},
                        {"git_pull_all": ["manage.py", "git_pull_all"]},
                        # {"background_tasks": ["manage.py", "process_tasks"]},
                        )
    cleanup_tasks = []
    app_root_folder_name = "server_for_django_15_and_below"


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    UfsStarterWithSqlite().start_iconized_applications()
