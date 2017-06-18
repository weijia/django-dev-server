import json
import os
import sys

import annoying
import dateutil
import pkg_resources
import pytz
from ufs_tools import get_folder
from ufs_tools.app_tools import get_executable_folder
from ufs_tools.short_decorator.ignore_exception import ignore_exc

from django_build.package_configs.base import PackageConfigBase
from djangoautoconf import DjangoAutoConf
from djangoautoconf.auto_conf_utils import get_module_path, enum_folders, enum_modules


def import_sub_module(name):
    __import__(name)
    return sys.modules[name]


def remove_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


class DjangoPackager(PackageConfigBase):
    total_settings_py = "local/total_settings.py"

    def __init__(self):
        super(DjangoPackager, self).__init__()
        # # Create data.db for SQLITE so build process can run with SQLITE
        # os.environ["POSTGRESQL_ROOT"] = ""
        remove_if_exists(self.total_settings_py)
        # self.excludes = []
        self.include_files = [
            ("local", "local"),
            ("scripts", "scripts"),
            ("server_base_packages/distutils", "distutils"),
            ("server_base_packages/pkg_resources", "pkg_resources"),
            # (get_module_path(pkg_resources), "pkg_resources"),
            # Not sure why the following is not included as in includes.
            # (get_module_path(dateutil), "dateutil"),
            # (get_module_path(annoying), "annoying"),
            # Required for pytz, otherwise, although build will be done, there will be timezone not found error in
            # runtime Used by pytz to load time zone info in zoneinfo folder
            # (get_module_path(pytz), "pytz"),
        ]

        self.force_include_file = [
            "pytz",
            "dateutil",
            "django_filters",
            "django",
            "cherrypy",
            "redis",
            "requests_oauthlib",
            "oauth2",
            "jinja2",
            "email",  # Use this to include all modules below email.
            "nine",
            'wsgiref',
            'annoying',
            'openid',
            'ufs_tools',
            'nonefield',
            'tastypie',
            'django_redis',
            'oauthlib',
        ]

        self.force_include_module = [
            # 'htmlentitydefs',
            # 'HTMLParser',
            # 'markupbase',
            # 'shortuuid',
            # 'persisting_theory',
            # 'csv',
            # 'appconf',
            # 'annoying',
            # 'html2text',
            # 'requests',
            # 'openid',
            'oauthlib',
            # 'markdown',
            # 'dateutil',
            # 'ufs_tools',
            # 'tablib',
            # 'diff_match_patch',
            # 'daphne',
            # 'tendo',
            # 'win32file',
            # 'git',
            # 'smmap',
            # 'gitdb',
            # '_multiprocessing',
            # 'multiprocessing',
            # 'evernote',
            # 'thrift',
            # 'tastypie',
            # 'jwt',
            # 'requests_oauthlib',
            # 'braces',
            # 'jira',
            # 'imghdr',
            "jwt",
            "requests_oauthlib",
            # "django",
            # 'ufs_tools.tuple_tools',
            'service_identity',
        ]

    def prepare(self):

        DjangoAutoConf.set_settings_env()
        import django
        django.setup()

        from django.conf import settings
        # include_files.extend(ModuleDescriptor().get_module_list_from_name("djangoautoconf"))

        # Include django by folder, for the following 2 reasons
        # 1. we need django template files which is not python modules
        # 2. Django module will include some module by a flag to check whether it is py3, but in cx_Freeze,
        # it can not detect such flag?
        # self._add_module_to_include_files("django")
        # self._add_module_to_include_files("cherrypy")
        # self._add_module_to_include_files("redis")
        for i in self.force_include_file:
            self._add_module_to_include_files(i)

        for installed_app in settings.INSTALLED_APPS:
            app_root_name = self.get_top_module(installed_app)
            self._add_module_to_include_files(app_root_name)

            self._include_default_files_in_django_app(app_root_name)

        new_modules = sys.modules.keys()

        for module in new_modules:
            app_root_name = self.get_top_module(module)
            self._add_module_to_includes(app_root_name)

        for m in self.force_include_module:
            self._add_module_to_includes(m)

        os.system(os.path.join(get_executable_folder(), "scripts/collectstatic.bat"))
        # os.system(os.path.join(root_folder, "scripts/collectcmd.bat"))
        os.system(sys.executable + " ./manage.py dump_settings")

    def get_top_module(self, installed_app):
        app_root_name = installed_app
        if "." in installed_app:
            app_root_name = installed_app.split(".")[0]
        return app_root_name

    def _include_default_files_in_django_app(self, django_app_name):
        for django_sub_module in ['urls', 'views', 'admin', 'api', 'models', 'forms', 'decorators', 'mixins',
                                  'management', 'migrations']:
            self._import_django_sub_module(django_app_name, django_sub_module)

        self._import_modules_in_urls(django_app_name)

    def _import_modules_in_urls(self, django_sub_module):
        #########
        # import modules from url.py
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
    def _import_django_sub_module(self, django_app_name, django_sub_module):
        # print django_app_name + "." + django_sub_module
        sub_module_import_name = django_app_name + "." + django_sub_module
        module = import_sub_module(sub_module_import_name)
        if django_sub_module == "management":
            command_folder = os.path.join(get_folder(module.__file__), "commands")
            if os.path.exists(command_folder):
                for module_name in enum_modules(command_folder):
                    __import__(sub_module_import_name + ".commands." + module_name)

    def get_executable_names(self):
        app_list = [
            'starter',
            'basic_starter',
            'manage',
            'cherrypy_server',
        ]

        additional_config_json_file_path = "local/additional_exe_config.json"
        if os.path.exists(additional_config_json_file_path):
            additional_exe_config_file = open(additional_config_json_file_path)
            additional_config = json.load(additional_exe_config_file)
            app_list.extend(additional_config["additional_apps"])
        return app_list

    def post_setup(self):
        remove_if_exists(self.total_settings_py)
