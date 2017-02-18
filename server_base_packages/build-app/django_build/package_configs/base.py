# noinspection PyMethodMayBeStatic
import os

from djangoautoconf.auto_conf_utils import get_module_path, get_source_filename


class PackageConfigBase(object):

    def __init__(self):
        super(PackageConfigBase, self).__init__()
        self.includes = []
        self.excludes = [
            "distutils",
            "pkg_resources",
            'cffi',
            '_cython_0_21',
            'urllib.parse',  # Import this will cause max recursion error
            'ndg',  # Not a valid module?
            '_openssl',  # Not a valid module?
            'certifi',  # Not a valid module?
            'zope',  # Include by dir
            '_virtualenv_distutils',  # Include by dir
            'collections.abc',
            'collections.sys',
            'cStringIO.errno',
            'cStringIO.sys',
            'distutils.archive_util',
            'mock',  # So include distutils will not report error
        ]
        self.include_files = []
        self.zip_includes = []

    def prepare(self):
        pass

    def get_include_files_or_folders_with_target(self):
        return self.include_files

    def get_include_module_names(self):
        return self.includes

    def get_excluded_module_names(self):
        return self.excludes

    def get_executable_names(self):
        return []

    def post_setup(self):
        pass

    def _get_include_file_config(self, app_root_name):
        include_config = None
        try:
            app_module = __import__(app_root_name, fromlist="dummy")
            module_file_full_path = app_module.__file__
            if self.is_folder_module(module_file_full_path):
                include_config = (get_source_filename(module_file_full_path),
                                  get_source_filename(os.path.basename(module_file_full_path)))
            else:
                include_config = (os.path.dirname(module_file_full_path), app_root_name)
        except Exception, e:
            pass
        return include_config

    def _add_module_to_include_files(self, app_root_name):
        if not self.is_folder_module(app_root_name):
            self.includes.append(app_root_name)
        else:
            if (app_root_name not in self.includes) and (app_root_name not in self.excludes):
                self.excludes.append(app_root_name)
            include_config = self._get_include_file_config(app_root_name)
            if include_config:
                self.include_files.append(include_config)

    def _add_module_to_includes(self, module_name):
        if (module_name not in self.includes) and (module_name not in self.excludes):
            self.includes.append(module_name)

    # noinspection PyMethodMayBeStatic
    def is_folder_module(self, module_file_full_path):
        return os.path.basename(module_file_full_path) != "__init__.pyc"
