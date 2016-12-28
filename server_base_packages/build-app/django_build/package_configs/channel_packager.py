from django_build.package_configs.base import PackageConfigBase


class ChannelPackager(PackageConfigBase):
    def get_include_module_names(self):
        return [
            'asgiref.inmemory',
            'asgiref.wsgi',
            'asgiref.conformance',
            'asgiref.base_layer',
        ]
