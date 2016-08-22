from django_build.app_freeze_config import get_iconizer_resources
from django_build.package_configs.qt_packager import QtPackager


class IconizerPackage(QtPackager):
    def get_include_files_or_folders_with_target(self):
        res = [self.get_include_config("iconizer")]
        res.extend(get_iconizer_resources())
        return res





