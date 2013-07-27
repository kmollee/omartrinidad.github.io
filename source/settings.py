"""Settings for pelican."""

# This can also be the absolute path to a theme that you downloaded
THEME = 'darktheme'
#SITESUBTITLE = 'Dreaming with a different and new Mexico'
SITESUBTITLE = 'This site is under construction'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'UTC'

# Pelican will take the ``Date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
# ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

AUTHOR = 'omartrinidad'
SITENAME = 'Omar swap file'
SITEURL = 'http://omartrinidad.github.io'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)

SOCIAL = (
        ('Twitter', 'http://twitter.com/omar_trinidad'),
        ('Facebook', 'http://facebook.com/pilu.omar'),
        ('LinkedIn', 'http://mx.linkedin.com/in/omartrinidad'),
        ('Goodreads', 'http://www.goodreads.com/user/show/17567302-omar-trinidad-guti-rrez-m-ndez'),
)

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
DISQUS_SITENAME = 'omarswapfile'
GITHUB_URL = 'http://github.com/omartrinidad/omartrinidad.github.io'
TWITTER_USERNAME = 'omar_trinidad'

