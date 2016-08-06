import json
import os
import sys

import pkg_resources
import pytz
from ufs_tools import get_folder
from ufs_tools.short_decorator.ignore_exception import ignore_exc

from django_build.package_configs.base import PackageConfigBase
from djangoautoconf import DjangoAutoConf
from djangoautoconf.auto_conf_utils import get_module_path, enum_folders, enum_modules


def remove_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


class DjangoPackager(PackageConfigBase):
    total_settings_py = "local/total_settings.py"

    def __init__(self):
        super(DjangoPackager, self).__init__()
        # Create data.db for SQLITE so build process can run with SQLITE
        os.environ["POSTGRESQL_ROOT"] = ""
        remove_if_exists(self.total_settings_py)
        self.excludes = []
        self.include_files = [
            ("local", "local"),
            ("scripts", "scripts"),
            ("server_base_packages/distutils", "distutils"),
            (get_module_path(pkg_resources), "pkg_resources"),
            # Required for pytz, otherwise, although build will be done, there will be timezone not found error in
            # runtime Used by pytz to load time zone info in zoneinfo folder
            (get_module_path(pytz), "pytz"),
        ]
        self.excludes = [
            "pytz",
            "distutils",
            "pkg_resources",
        ]
        self.include_module_names = [
            'htmlentitydefs',
            'HTMLParser',
            'markupbase',
            'shortuuid',
            'persisting_theory',
            'csv',
            'appconf',
            'annoying',
            'html2text',
            'requests',
            'openid',
            'oauthlib',
            'markdown',
            'dateutil',
            'ufs_tools',
            'tablib',
            'diff_match_patch',
            'daphne',
            'tendo',
            'win32file',
            'git',
            'smmap',
            'gitdb',
            '_multiprocessing',
            'multiprocessing',
            'evernote',
            'thrift',
            'tastypie',
        ]

    def prepare(self):

        DjangoAutoConf.set_settings_env()
        import django
        django.setup()

        from django.conf import settings
        # include_files.extend(ModuleDescriptor().get_module_list_from_name("djangoautoconf"))

        old_modules = sys.modules.keys()

        for installed_app in settings.INSTALLED_APPS:
            app_root_name = installed_app
            if "." in installed_app:
                app_root_name = installed_app.split(".")[0]

            self.excludes.append(app_root_name)
            include_config = self.get_include_config(app_root_name)
            if include_config:
                self.include_files.append(include_config)

            self.include_default_files_in_django_app(app_root_name)

        new_modules = sys.modules.keys()

        for i in new_modules:
            if i not in old_modules:
                module = i
                if "." in i:
                    module = module.split(".")[0]
                if module not in self.excludes:
                    self.include_module_names.append(module)

        # os.system(os.path.join(root_folder, "scripts/syncdb.bat"))
        # os.system(sys.executable + " ./manage.py migrate")
        # os.system(os.path.join(root_folder, "scripts/collectstatic.bat"))
        # os.system(os.path.join(root_folder, "scripts/collectcmd.bat"))
        os.system(sys.executable + " ./manage.py dump_settings")

    def include_default_files_in_django_app(self, django_app_name):
        for django_sub_module in ['urls', 'views', 'admin', 'api', 'models', 'forms', 'decorators', 'mixins',
                                  'management', 'migrations']:
            self.import_django_sub_module(django_app_name, django_sub_module)

        self.import_modules_in_urls(django_app_name)

    def import_modules_in_urls(self, django_sub_module):
        #########
        # import modules from url
        #########
        try:
            module_str = django_sub_module + ".urls"
            url_module = __import__(module_str)
            try:
                url_module = getattr(url_module, "urls")
                url_patterns = getattr(url_module, "urlpatterns")
            except AttributeError:
                # import traceback
                # traceback.print_exc()
                url_patterns = []
        except ImportError:
            url_patterns = []
            # import traceback
            # traceback.print_exc()

    # noinspection PyMethodMayBeStatic
    @ignore_exc
    def import_django_sub_module(self, django_app_name, django_sub_module):
        # print django_app_name + "." + django_sub_module
        sub_module_import_name = django_app_name + "." + django_sub_module
        module = __import__(sub_module_import_name)
        if django_sub_module == "management":
            command_folder = os.path.join(get_folder(module.__file__), "commands")
            if os.path.exists(command_folder):
                for module_name in enum_modules(command_folder):
                    __import__(sub_module_import_name + "commands." + module_name)

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
        return self.include_files

    def get_include_module_names(self):
        return self.include_module_names

    def post_setup(self):
        remove_if_exists(self.total_settings_py)
