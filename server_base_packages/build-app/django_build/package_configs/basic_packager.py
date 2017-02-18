import os
from os.path import dirname

import _tkinter

from django_build.package_configs.base import PackageConfigBase


class BasicPackager(PackageConfigBase):
    def prepare(self):
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

