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

# Blogroll
LINKS =  (("Matt O'Brien", 'http://www.mattobrien.me/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "/home/Prateek/pelican-themes/lannisport"
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
'extra/CNAME': {'path':'CNAME'}}