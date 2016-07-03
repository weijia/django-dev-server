import logging

from iconizer.django_in_iconizer.django_starter import DjangoStarter

log = logging.getLogger(__name__)


class UfsBasicStarter(DjangoStarter):

    def get_background_tasks(self):
        return (
            self.django_server.get_task_descriptor("git_pull_all"),
            # self.django_server.get_task_descriptor("drop_tagger"),
            # {"background_tasks": ["manage_with_conf.py", "process_tasks"]},
            # {"ipynb": ["manage.py", "shell_ipynb"]},
            # {"ipynb": ["jupyter-notebook.exe", "--config=ipython_config.py"]},
            # {"clipboard_monitor": ["manage.py", "clipboard_monitor_task"]},
            # {"web_server": ["cherrypy_server.py", ]}),
            # {"ipynb": ["jupyter-notebook.exe", "--config=ipython_config.py"]})
        )

    def sync_to_main_thread(self):
        self.init_ufs_db()

    def get_frontend_task_descriptor(self):
        # return self.django_server.get_run_server_task_descriptor(["0.0.0.0:8110"])
        return self.django_server.get_run_server_task_descriptor()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    UfsBasicStarter().start_iconized_applications()
