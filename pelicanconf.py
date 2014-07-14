#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Prateek_Singhal'
SITENAME = u'patthebug'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'
PLUGIN_PATHS = ['/home/Prateek/pelican/pelican-plugins']
PLUGINS = ['render_math']

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
SITELOGO = '/home/Prateek/pelican/USF22.png'
GITHUB_URL = 'https://github.com/patthebug'

# Blogroll
LINKS =  (("Matt O'Brien", 'http://www.mattobrien.me/'),)

# Social widget
SOCIAL = (('https://www.linkedin.com/pub/prateek-singhal/16/761/a4', '#'),
          ('https://github.com/patthebug', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "/home/Prateek/pelican-themes/gum"
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
'extra/CNAME': {'path':'CNAME'}}