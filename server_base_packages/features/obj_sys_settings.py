INSTALLED_APPS += (
    'simplemenu',
    'tagging',
    'geoposition',
    'obj_sys',
    'ajax_search',
)

AJAX_SEARCH_HELPER = 'obj_sys.ufs_search_helper.search_helper'
SEARCH_RESULT_TEMPLATE = 'obj_sys/ufs_search.html'
AJAX_SEARCH_LIMIT = 10