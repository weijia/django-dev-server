class Version(object):
    def __init__(self):
        self.version = "1.0"


def get_distribution(param):
    return Version()


# For django-compat start
class Provider(object):
    version = "1.0"


def get_provider(moduleOrReq):
    return Provider()


class Requirement:
    def __init__(self, project_name, specs, extras):
        pass

    @staticmethod
    def parse(s):
        reqs = list()
        return reqs


class DistributionNotFound(object):
    pass
# For django-compat end
