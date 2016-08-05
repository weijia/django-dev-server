import json
import os

from django_build.app_freeze_config import create_executable_from_app_name, get_iconizer_resources
from django_build.module_processor import ModuleDescriptor
from django_build.package_configs.base import PackageConfigBase


class IconizerPackage(PackageConfigBase):
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
        res = [ModuleDescriptor().get_module_list_from_name("iconizer")]
        res.extend(get_iconizer_resources())
        return res

    def get_include_module_names(self):
        return "PyQt4.QtCore",




