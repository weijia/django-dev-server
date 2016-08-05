from cx_Freeze import setup

from django_build.package_configs.basic_packager import BasicPackager
from django_build.package_configs.django_packager import DjangoPackager
from django_build.package_configs.iconizer_packager import IconizerPackage
from django_build.packager_utils import get_build_exe_params, get_executables, run_packager_post_setup


def main():

    packager_list = [
        BasicPackager(),
        IconizerPackage(),
        DjangoPackager(),
    ]

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
