from djangoautoconf.auto_conf_utils import get_module_path

from django_build.package_configs.base import PackageConfigBase
import zope.interface


class RedisPackager(PackageConfigBase):

    def get_include_files_or_folders_with_target(self):
        return [
                    (get_module_path(zope.interface), "zope/interface"),
                    ("other-apps/", "other-apps"),
                ]

