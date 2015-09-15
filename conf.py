#!/usr/bin/env python
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.curdir)

AUTHOR = 'Mikael Hernrup'
SITENAME = 'NowThinkDammit'
SITEURL = 'http://hernrup.github.io/hernrup_se_ntd/'

PATH = 'content'
OUTPUT_PATH = '/output/'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Stockholm'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
RELATIVE_URLS = True
