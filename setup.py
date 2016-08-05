# from setuptools import find_packages
import json
import os
import pprint
import sys
from distutils import dir_util
from distutils import errors
from distutils import log
from distutils import version

import certifi
import django
import pkg_resources
import pytz

import zope.interface
import _tkinter
from os.path import dirname
from cx_Freeze import setup

from django_build.python_env_utils import ScriptExe
from ufs_tools import get_folder
from ufs_tools.basic_lib_tool import include
from ufs_tools.libtool import include_all
import ipykernel

include_all(__file__, "server_base_packages")
import iconizer

from djangoautoconf.auto_conf_utils import get_module_path, get_module_file_path, get_module_filename, \
    get_module_include_files_config
from djangoautoconf.setting_utils.app_folders import AppFolderUtil
from django_build.app_freeze_config import gen_executable_list, get_iconizer_resources, create_executable_from_app_name
from django_build.django_setup import DjangoCxFreezeBuildSpecGenerator
from djangoautoconf import DjangoAutoConf


total_setting_file_path = "local/total_settings.py"


def remove_if_exists(file_path):
    try:
        os.remove(file_path)
    except:
        pass


def main():
    remove_if_exists(total_setting_file_path)

    root_folder = get_folder(__file__)
    u = AppFolderUtil(root_folder)
    for folder in u.enum_app_folders():
        include(folder)

    # Create data.db for SQLITE so build process can run with SQLITE
    os.environ["POSTGRESQL_ROOT"] = ""

    DjangoAutoConf.set_settings_env()

    from django.conf import settings

    django.setup()

    ###########################
    # Add python module that is not automatically included in the build below. Such as Django app
    # file with special names other than: models, urls, admin, views etc.
    ###########################
    includes = [
        "PyQt4.QtCore",
        "yaml",
        # For Cherrypy
        # "django.contrib.messages",
        "email",
        "email.message",
        "cherrypy",
        #"iconizer",
        "django.core.management",
        "django.core.management.commands.syncdb",
    ]

    app_list = [
        'starter',
        'manage',
        'cherrypy_server',
    ]

    add_additional_apps(app_list)

    include_files = []

    include_files.extend(get_iconizer_resources())

    include_files.extend([
        ("local", "local"),
        # Required for pytz, otherwise, although build will be done, there will be timezone not found error in runtime
        # Used by pytz to load time zone info in zoneinfo folder
        (get_module_path(pytz), "pytz"),
        (get_module_path(ipykernel), "ipykernel"),
        (get_module_path(iconizer), "iconizer"),
        (get_module_path(zope.interface), "zope/interface"),
        (get_module_path(pkg_resources), "pkg_resources"),
        (get_module_path(certifi), "certifi"),
        ("server_base_packages/distutils", "distutils"),
        get_module_include_files_config(dir_util, "distutils"),
        get_module_include_files_config(errors, "distutils"),
        get_module_include_files_config(log, "distutils"),
        get_module_include_files_config(version, "distutils"),
        ("ipython_config.py", "ipython_config.py"),
        ScriptExe("jupyter.exe").get_the_include_files_config_for_script_exe(),
        ScriptExe("jupyter-notebook.exe").get_the_include_files_config_for_script_exe(),

        # ("server_base_packages/pkg_resources", "pkg_resources"),
        # #("libs/allauth/fixtures/initial_data.json", "initial_data.json"),
        # ("libs/zlib1.dll", "libs/zlib1.dll"),
        # ("libs/regex2.dll", "libs/regex2.dll"),
        # ("libs/magic1.dll", "libs/magic1.dll"),
        # ("tornado_app.bat", "tornado.bat"),
        # ("activate_app.bat", "activate.bat"),
    ])

    build_exe_dir = "../build/%s" % os.path.basename(os.path.dirname(__file__))

    build_exe_params = {
        "includes": includes,
        'include_files': include_files,
        "bin_excludes": [],
        "build_exe": build_exe_dir,
        "zip_includes": [],
        # https://bitbucket.org/anthony_tuininga/cx_freeze/issues/127/collectionssys-error
        'excludes': ['collections.abc',
                     'collections.sys',
                     'cStringIO.errno',
                     'cStringIO.sys',
                     'distutils.archive_util',
                     'mock',  # So include distutils will not report error
                     'certifi',
                     ]
        # "packages": find_packages(),
        # "create_shared_zip": False,
    }

    # os.system(os.path.join(root_folder, "scripts/syncdb.bat"))
    os.system(sys.executable + " ./manage.py migrate")
    os.system(os.path.join(root_folder, "scripts/collectstatic.bat"))
    os.system(os.path.join(root_folder, "scripts/collectcmd.bat"))
    os.system(sys.executable + " ./manage.py dump_settings")

    # Need to remove port_v3 for QT for cx_freeze when packaging PyQt
    set_env_var_for_tkinter_in_exe()

    DjangoCxFreezeBuildSpecGenerator().gen_spec(settings, build_exe_params)

    final_script_list = gen_executable_list(app_list)
    final_script_list.append(create_executable_from_app_name("starter"))
    # final_script_list.append(create_executable_from_app_name("starter", base="Win32GUI"))
    # pprint.pprint(build_exe_params)
    setup(
        version="0.1",  # This is required or build process will have exception.
        description="application starter",
        options={"build_exe": build_exe_params},
        executables=final_script_list,
        # include_package_data=True,
        # package_data = {'':['*.*', 'templates/*.*']},
        # packages = find_packages(),
    )

    remove_if_exists(total_setting_file_path)


def add_additional_apps(app_list):
    additional_config_json_file_path = "local/additional_exe_config.json"
    if os.path.exists(additional_config_json_file_path):
        additional_exe_config_file = open(additional_config_json_file_path)
        additional_config = json.load(additional_exe_config_file)
        app_list.extend(additional_config["additional_apps"])


def set_env_var_for_tkinter_in_exe():
    """
    For fixing error of the following:
    _tkinter.TclError: Can't find a usable init.tcl in the following directories:
    c:/python27/lib/tcl8.5 D:/work/venv/django18/lib/tcl8.5 D:/work/venv/lib/tcl8.5 D:/work/venv/django18/library D:/work/venv/library D:/work/venv/tcl8.5.15/library D:/work/tcl8.5.15/library
    This probably means that Tcl wasn't installed properly.
    :return: None
    """
    python_dir = dirname(dirname(_tkinter.__file__))
    tcl_lib_path_name = "tcl/tcl" + _tkinter.TCL_VERSION
    tk_lib_path_name = "tcl/tk" + _tkinter.TCL_VERSION
    os.environ["TCL_LIBRARY"] = os.path.join(python_dir, tcl_lib_path_name)
    os.environ["TK_LIBRARY"] = os.path.join(python_dir, tk_lib_path_name)


if __name__ == "__main__":
    main()
