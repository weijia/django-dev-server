import os

import sys

import pytz
from cx_Freeze import Executable

from djangoautoconf.auto_conf_utils import get_module_path
from ufs_tools import filetools

from iconizer.qtconsole.fileTools import find_resource_in_pkg


def create_executable_from_app_name(app_param, base=None):
    if type(app_param) != tuple:
        app_full_name = app_param + ".py"
        app_path = filetools.find_filename_in_app_framework_with_pattern(app_full_name)
        if app_path is None:
            return None
            # print "app:", app_path
        if base is None:
            return Executable(script=app_path)
        else:
            return Executable(script=app_path, base=base)
    else:
        app_full_name = app_param[0] + ".py"
        app_path = filetools.find_filename_in_app_framework_with_pattern(app_full_name)
        # print "app with target:", app_path
        return Executable(script=app_path, targetName=app_param[1])


def gen_executable_list(script_list):
    executable_list = []
    for i in script_list:
        app = create_executable_from_app_name(i)
        if app is None:
            continue
        executable_list.append(app)
    return executable_list


def get_pytz_files():
    path_base = get_module_path(pytz)
    exe_path = os.path.dirname(sys.executable)
    if "Scripts" in exe_path:
        exe_path = os.path.dirname(exe_path)
    # path_base = os.path.join(exe_path, "Lib\\site-packages\\pytz\\zoneinfo\\")
    skip_count = len(path_base)
    zip_includes = [(path_base, "pytz/zoneinfo/")]
    for root, sub_folders, files in os.walk(path_base):
        for file_in_root in files:
            zip_includes.append(
                ("{}".format(os.path.join(root, file_in_root)),
                 "{}".format(os.path.join("pytz/zoneinfo", root[skip_count:], file_in_root))
                 )
            )
    return zip_includes


def get_iconizer_resources():
    result = []
    for i in ["gf-16x16.png", "list_window.ui", "droppable.ui", "notification.ui"]:
        result.append((find_resource_in_pkg(i), i))
    return result
