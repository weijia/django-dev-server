import pkgutil

import django


class ModuleDescriptor(object):
    def __init__(self):
        super(ModuleDescriptor, self).__init__()
        self.module_list = []

    def update_module_list(self, package):
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, package.__name__+"."):
            # print "Found submodule %s (is a package: %s)" % (modname, ispkg)
            if ispkg:
                try:
                    module = __import__(modname, fromlist="dummy")
                    self.update_module_list(module)
                except:
                    pass
            else:
                if modname not in self.module_list:
                    self.module_list.append(modname)

    def get_module_list(self, package):
        self.module_list = []
        self.update_module_list(package)
        return self.module_list

    def get_module_list_from_name(self, package_name):
        package = __import__(package_name, fromlist="dummy")
        return self.get_module_list(package)


if __name__ == '__main__':
    from pkg_resources import resource_listdir
    import django.conf.locale as django_locale
    # Itemize data files under proj/resources/images:
    print django_locale.__file__
    print resource_listdir('django.conf.locale', '')
    # Get the data file bytes:
    # print resource_string('proj.resources.images', 'pic2.png').encode('base64')
    # for m in ModuleDescriptor().get_module_list(django):
    #     print m
