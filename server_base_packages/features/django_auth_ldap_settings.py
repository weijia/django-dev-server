from django_auth_ldap.config import LDAPSearch
import ldap

from djangoautoconf.local_key_manager import ConfigurableAttributeGetter, get_local_key

AUTHENTICATION_BACKENDS = (
    'djangoautoconf.auth.ldap_backend_wrapper.LDAPBackendWrapper',
    #'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
# !!!!!Do not uncomment the following codes, it is just used to find the LDAPBackend module. Uncomment
# the following line will cause django mis configure and it will not start.
# from django_auth_ldap.backend import LDAPBackend

getter = ConfigurableAttributeGetter("ldap_settings", "webmanager.keys_defaults")
AUTH_LDAP_SERVER_URI = getter.get_attr("auth_ldap_server_uri")
# ldap.set_option(ldap.OPT_DEBUG_LEVEL, 4095)


AUTH_LDAP_BIND_PASSWORD = get_local_key("ldap_settings.ldap_bind_password")
AUTH_LDAP_BIND_DN = get_local_key("ldap_settings.ldap_dn")
search_str = getter.get_attr("search_str")
AUTH_LDAP_USER_SEARCH = LDAPSearch(search_str, ldap.SCOPE_SUBTREE, "uid=%(user)s")
