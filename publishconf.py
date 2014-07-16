#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://patthebug.github.io/pelican'
SITEURL = 'http://prateeksinghal.com'
RELATIVE_URLS = False
SITELOGO = '/home/Prateek/pelican/USF22.png'
LINKEDIN_URL = 'https://www.linkedin.com/pub/prateek-singhal/16/761/a4'
SITETAGLINE = 'randomness is beautiful'
GITHUB_URL = 'https://github.com/patthebug'
FACEBOOK_URL = 'https://www.facebook.com/prateek2686'
SITEDESCR = 'Adventures in Data Science, learning something new, every day !'
DISQUS_SITENAME = 'patthebug'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-51399126-1"
