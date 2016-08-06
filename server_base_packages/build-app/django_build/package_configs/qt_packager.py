import os
from os.path import dirname

import _tkinter

from django_build.package_configs.base import PackageConfigBase


class QtPackager(PackageConfigBase):
    def get_include_module_names(self):
        return "PyQt4.QtCore",