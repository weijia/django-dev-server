# noinspection PyMethodMayBeStatic
from djangoautoconf.auto_conf_utils import get_module_path


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
            include_config = (get_module_path(app_module), app_root_name)
        except:
            pass
        return include_config
