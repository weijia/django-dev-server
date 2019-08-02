from django.conf.urls import url, include

from djangoautoconf.auto_conf_urls import add_to_root_url_pattern

add_to_root_url_pattern(
    (
        # View URLs
        url(r'^fobi/', include('fobi.urls.view')),

        # Edit URLs
        url(r'^fobi/', include('fobi.urls.edit')),
        url(r'^fobi/plugins/form-handlers/db-store/',
            include('fobi.contrib.plugins.form_handlers.db_store.urls')),
    )
)
