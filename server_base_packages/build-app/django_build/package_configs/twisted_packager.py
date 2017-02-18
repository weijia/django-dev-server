from django_build.package_configs.base import PackageConfigBase


class TwistedPackager(PackageConfigBase):
    def get_include_module_names(self):
        return [
            # 'twisted',
            'txaio',
        ]

    def get_include_files_or_folders_with_target(self):
        # return super(TwistedPackager, self).get_include_files_or_folders_with_target()
        return [self._get_include_file_config("twisted")]
