server_django_15_and_below
===========================


Add URL pattern in project
===========================
1. App with default_settings.py will be added automatically
2. Use add_url_pattern to add URL pattern and target view/url patterns


Folders
===========================
server_base_packages: git repositories the basic server depends on.
    Codes in here will be changed regardless of what applications are running in this server.
    Basic server will not run without the packages in this folder

external_app_repos: additional repositories can be place here. 
    They should be managed in separate repository.
    Then they will not impact the code modification of the base server.

