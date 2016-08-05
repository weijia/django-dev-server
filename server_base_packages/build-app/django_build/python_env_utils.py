import os
import sys


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
