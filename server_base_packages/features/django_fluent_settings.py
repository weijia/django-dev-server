INSTALLED_APPS += (
    # CMS parts
    'fluent_blogs',
    'fluent_blogs.pagetypes.blogpage',
    'fluent_pages',
    'fluent_pages.pagetypes.fluentpage',
    'fluent_pages.pagetypes.flatpage',
    'fluent_pages.pagetypes.redirectnode',
    'fluent_comments',
    'fluent_contents',
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    'fluent_contents.plugins.gist',
    'fluent_contents.plugins.oembeditem',
    'fluent_contents.plugins.picture',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.sharedcontent',
    'fluent_contents.plugins.text',

    # Support libs
    'analytical',
    'any_imagefield',
    'any_urlfield',
    'axes',
    'categories_i18n',
    'crispy_forms',
    'django_comments',
    'django_wysiwyg',
    'django.contrib.redirects',
    'filebrowser',
    'mptt',
    'parler',
    'polymorphic',
    'polymorphic_tree',
    'slug_preview',
    'staff_toolbar',
    'sorl.thumbnail',
    'taggit',
    'taggit_selectize',
    'threadedcomments',
    'tinymce',

    # and enable the admin
    'fluent_dashboard',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
)
