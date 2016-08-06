from cx_Freeze import setup
from ufs_tools.python_app_utils.base import AppBase
import sys

def main():
    AppBase().add_default_module_path()

    from django_build.package_configs.basic_packager import BasicPackager
    from django_build.package_configs.django_packager import DjangoPackager
    from django_build.package_configs.iconizer_packager import IconizerPackage
    from django_build.packager_utils import get_build_exe_params, get_executables, run_packager_post_setup, \
        run_packager_prepare

    packager_list = [
        BasicPackager(),
        IconizerPackage(),
        DjangoPackager(),
    ]

    run_packager_prepare(packager_list)

    setup(
        version="0.1",  # This is required or build process will have exception.
        description="application starter",
        options={"build_exe": get_build_exe_params(packager_list)},
        executables=get_executables(packager_list),
        # include_package_data=True,
        # package_data = {'':['*.*', 'templates/*.*']},
        # packages = find_packages(),
    )

    run_packager_post_setup(packager_list)


if __name__ == "__main__":
    main()
