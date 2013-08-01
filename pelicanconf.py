#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'omartrinidad'
SITENAME = u'Omar swap file'
SITESUBTITLE = 'Website under construction'

SITEURL = 'http://omartrinidad.github.io'
STATIC_PATHS = ['images', ]

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False

# Added after pelican-quickstart
THEME = '/home/omartrinidad/projects/nerdpowa'

# Archives in the main menu.
MENUITEMS = (('Archives', '{0}/archives.html'.format(SITEURL)),
             ('About', '{0}/about.html'.format(SITEURL)),)

"""
SOCIAL = (
    ('Twitter', 'http://twitter.com/omar_trinidad'),
    ('Facebook', 'http://facebook.com/pilu.omar'),
    ('LinkedIn', 'http://mx.linkedin.com/in/omartrinidad'),
    ('Goodreads', 'http://www.goodreads.com/user/show/17567302-omar-trinidad-guti-rrez-m-ndez'),
)
"""

ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'


