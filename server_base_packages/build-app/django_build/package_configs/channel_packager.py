from djangoautoconf.auto_conf_utils import get_module_path

from django_build.package_configs.base import PackageConfigBase
import zope.interface

class ChannelPackager(PackageConfigBase):
    def get_include_module_names(self):
        return [
            'asgiref.inmemory',
            'asgiref.wsgi',
            'asgiref.conformance',
            'asgiref.base_layer',
        ]

    def get_include_files_or_folders_with_target(self):
        return [
                    (get_module_path(zope.interface), "zope/interface"),
                    ("server_base_packages/build-app/django_build/__init__.py", "zope/__init__.py"),
                ]

