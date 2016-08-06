import json
import os
import sys
import pytz

from django_build.package_configs.base import PackageConfigBase
from djangoautoconf import DjangoAutoConf
from djangoautoconf.auto_conf_utils import get_module_path


def remove_if_exists(file_path):
    try:
        os.remove(file_path)
    except:
        pass


class DjangoPackager(PackageConfigBase):
    total_settings_py = "local/total_settings.py"

    def prepare(self):
        # os.system(os.path.join(root_folder, "scripts/syncdb.bat"))
        # os.system(sys.executable + " ./manage.py migrate")
        # os.system(os.path.join(root_folder, "scripts/collectstatic.bat"))
        # os.system(os.path.join(root_folder, "scripts/collectcmd.bat"))
        os.system(sys.executable + " ./manage.py dump_settings")

    def get_executable_names(self):
        app_list = [
            'starter',
            'manage',
            'cherrypy_server',
        ]

        additional_config_json_file_path = "local/additional_exe_config.json"
        if os.path.exists(additional_config_json_file_path):
            additional_exe_config_file = open(additional_config_json_file_path)
            additional_config = json.load(additional_exe_config_file)
            app_list.extend(additional_config["additional_apps"])
        return app_list

    def get_include_files_or_folders_with_target(self):

        res = [
            ("local", "local"),
            # Required for pytz, otherwise, although build will be done, there will be timezone not found error in
            # runtime Used by pytz to load time zone info in zoneinfo folder
            (get_module_path(pytz), "pytz"),
        ]

        # Create data.db for SQLITE so build process can run with SQLITE
        os.environ["POSTGRESQL_ROOT"] = ""
        remove_if_exists(self.total_settings_py)
        DjangoAutoConf.set_settings_env()
        import django

        django.setup()
        from django.conf import settings
        # res.extend(ModuleDescriptor().get_module_list_from_name("djangoautoconf"))
        for installed_app in settings.INSTALLED_APPS:
            app_root_name = installed_app
            if "." in installed_app:
                app_root_name = installed_app.split(".")[0]

            include_config = self.get_include_config(app_root_name)
            if include_config:
                res.append(include_config)

        return res

    def post_setup(self):
        remove_if_exists(self.total_settings_py)
