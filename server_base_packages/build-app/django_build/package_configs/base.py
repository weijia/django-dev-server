# noinspection PyMethodMayBeStatic
class PackageConfigBase(object):
    def prepare(self):
        pass

    def get_include_files_or_folders_with_target(self):
        return []

    def get_include_module_names(self):
        return []

    def get_excluded_module_names(self):
        return []

    def get_executable_names(self):
        return []

    def post_setup(self):
        pass