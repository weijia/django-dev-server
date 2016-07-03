# from setuptools import find_packages
import os
import pprint
import sys
import django

from ufs_tools import get_folder
from ufs_tools.basic_lib_tool import include
from ufs_tools.libtool import include_all
from djangoautoconf.setting_utils.app_folders import AppFolderUtil
import _tkinter
from os.path import dirname
from cx_Freeze import setup

from django_build.app_freeze_config import gen_executable_list, get_pytz_files, \
    get_iconizer_resources

include_all(__file__, "server_base_packages")


root_folder = get_folder(__file__)
u = AppFolderUtil(root_folder)
for folder in u.enum_app_folders():
    include(folder)

from django_build.django_setup import DjangoCxFreezeBuildSpecGenerator

# Create data.db for SQLITE so build process can run with SQLITE
os.environ["POSTGRESQL_ROOT"] = ""

from djangoautoconf import DjangoAutoConf

DjangoAutoConf.set_settings_env()

from django.conf import settings


django.setup()


###########################
# Add python module that is not automatically included in the build below. Such as Django app
# file with special names other than: models, urls, admin, views etc.
###########################
includes = [
    # os.environ["DJANGO_SETTINGS_MODULE"], #rootapp
    "PyQt4.QtCore",
    "pkg_resources",  # Used by pytz to load time zone info in zoneinfo folder
    "yaml",
    # For Cherrypy
    # "django.contrib.messages",
    "email",
    "email.message",
    "cherrypy",
    "iconizer",
    "django.core.management",
    "django.core.management.commands.syncdb",
]

app_list = [
    'starter',
    'manage',
    'cherrypy_server',
]

include_files = []

include_files.extend(get_iconizer_resources())

include_files.extend([
    ("local", "local"),
    # #("libs/allauth/fixtures/initial_data.json", "initial_data.json"),
    # ("libs/zlib1.dll", "libs/zlib1.dll"),
    # ("libs/regex2.dll", "libs/regex2.dll"),
    # ("libs/magic1.dll", "libs/magic1.dll"),
    # ("tornado_app.bat", "tornado.bat"),
    # ("activate_app.bat", "activate.bat"),
])

excludefiles = []
zip_includes = get_pytz_files()
build_exe_dir = "../build/django-dev-server"

build_exe_params = {
    "includes": includes,
    'include_files': include_files,
    "bin_excludes": excludefiles,
    "build_exe": build_exe_dir,
    "zip_includes": zip_includes,
    # https://bitbucket.org/anthony_tuininga/cx_freeze/issues/127/collectionssys-error
    'excludes': ['collections.abc',
                 'collections.sys',
                 'cStringIO.errno',
                 'cStringIO.sys']
    # "packages": find_packages(),
    # "create_shared_zip": False,
}


# os.system(os.path.join(root_folder, "scripts/syncdb.bat"))
# os.system(sys.executable + " ./manage.py migrate")
# os.system(os.path.join(root_folder, "scripts/collectstatic.bat"))
# os.system(os.path.join(root_folder, "scripts/collectcmd.bat"))
# os.system(sys.executable + " ./manage.py dump_settings")

# Need to remove port_v3 for QT for cx_freeze when packaging PyQt


# Workarround for cx_freeze packaging cherrypy


python_dir = dirname(dirname(_tkinter.__file__))
tcl_lib_path_name = "tcl/tcl" + _tkinter.TCL_VERSION
tk_lib_path_name = "tcl/tk" + _tkinter.TCL_VERSION
os.environ["TCL_LIBRARY"] = os.path.join(python_dir, tcl_lib_path_name)
os.environ["TK_LIBRARY"] = os.path.join(python_dir, tk_lib_path_name)


DjangoCxFreezeBuildSpecGenerator().gen_spec(settings, build_exe_params)

final_script_list = gen_executable_list(app_list)
pprint.pprint(build_exe_params)
setup(
    version="0.1",  # This is required or build process will have exception.
    description="application starter",
    options={"build_exe": build_exe_params},
    executables=final_script_list,
    # include_package_data=True,
    # package_data = {'':['*.*', 'templates/*.*']},
    # packages = find_packages(),
)
