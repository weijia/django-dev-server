# noinspection PyMethodMayBeStatic
import os

from djangoautoconf.auto_conf_utils import get_module_path, get_source_filename


class PackageConfigBase(object):
    def prepare(self):
        pass

    def get_include_files_or_folders_with_target(self):
        return []

    def get_include_module_names(self):
        return []

    def get_excluded_module_names(self):
        return []

    def get_executable_names(self):
        return []

    def post_setup(self):
        pass

    def get_include_config(self, app_root_name):
        include_config = None
        try:
            app_module = __import__(app_root_name, fromlist="dummy")
            module_file_full_path = app_module.__file__
            if os.path.basename(module_file_full_path) != "__init__.pyc":
                include_config = (get_source_filename(module_file_full_path),
                                  get_source_filename(os.path.basename(module_file_full_path)))
            else:
                include_config = (os.path.dirname(module_file_full_path), app_root_name)
        except Exception, e:
            pass
        return include_config
