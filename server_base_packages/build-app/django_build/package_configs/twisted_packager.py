from django_build.package_configs.base import PackageConfigBase


class TwistedPackager(PackageConfigBase):
    def get_include_module_names(self):
        return [
            'twisted',
            'txaio',
        ]
