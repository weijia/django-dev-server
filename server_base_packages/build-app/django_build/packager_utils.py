import os

from django_build.app_freeze_config import create_executable_from_app_name


def get_executables(packager_list):
    executable_names = []
    for package in packager_list:
        executable_names = combine(executable_names, package.get_executable_names())

    res = []
    for app in executable_names:
        res.append(create_executable_from_app_name(app))

    return res


def get_build_exe_params(packager_list):
    build_exe_dir = "../build_new/%s" % os.path.basename(os.path.dirname(__file__))

    ###########################
    # Add python module that is not automatically included in the build below. Such as Django app
    # file with special names other than: models, urls, admin, views etc.
    ###########################
    includes = []
    include_files = []
    excludes = []

    for package in packager_list:
        includes = combine(includes, package.get_include_module_names())
        include_files = combine(include_files, package.get_include_files_or_folders_with_target())
        excludes = combine(excludes, package.get_excluded_module_names())

    return {
        "includes": includes,
        'include_files': include_files,
        "bin_excludes": [],
        "build_exe": build_exe_dir,
        "zip_includes": [],
        'excludes': excludes
        # "packages": find_packages(),
        # "create_shared_zip": False,
    }


def combine(base_list, new_item_list):
    base_list.extend(new_item_list)
    return list(tuple(base_list))


def run_packager_post_setup(packager_list):
    for package in packager_list:
        package.post_setup()

