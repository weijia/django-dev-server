import os
import sys

from ufs_tools import main_is_frozen
from ufs_tools.app_tools import get_executable_folder


class ScriptExe(object):

    def __init__(self, script_name):
        super(ScriptExe, self).__init__()
        self.script_name = script_name

    # noinspection PyMethodMayBeStatic
    def get_python_executable(self):
        return sys.executable

    def get_python_script_exe(self):
        return os.path.join(os.path.dirname(self.get_python_executable()), self.script_name)

    def get_the_include_files_config_for_script_exe(self):
        return self.get_python_script_exe(), self.script_name


class FrozenApp(object):
    def __init__(self):
        super(FrozenApp, self).__init__()
        self.root_folder = get_executable_folder()

    def get_exe_full_path(self, exe_name):
        return os.path.join(self.root_folder, exe_name)


class ScriptApp(object):
    def get_exe_full_path(self, exe_name):
        script_exe = ScriptExe(exe_name)
        if os.path.exists(script_exe.get_python_script_exe()):
            return script_exe.get_python_script_exe()
        raise "Script now found"


class AppWrapper(object):
    def __init__(self):
        super(AppWrapper, self).__init__()
        if main_is_frozen():
            self.app = FrozenApp()
        else:
            self.app = ScriptApp()

    def get_exe_full_path(self, exe_name):
        return self.app.get_exe_full_path(exe_name)
