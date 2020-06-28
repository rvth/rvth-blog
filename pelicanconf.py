#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ruth'
SITENAME = "Ruth's Blog"
SITEURL = 'https://rvth.blog'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = "%b %d, %Y"
USER_LOGO_URL = "http://i.imgur.com/zzCRZUH.jpg"

THEME = "voce"

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'


EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}

#Theme specific
GOOGLE_ANALYTICS_ID = "UA-123456-7"
GOOGLE_ANALYTICS_PROP = "siteurl.com"
TAGLINE = "Site Tagline"
MANGLE_EMAILS = False
GLOBAL_KEYWORDS = ("keywords",)


SOCIAL = (
    ("Feed", "https://siteurl.com/feeds/all.atom.xml"),
    ("GitHub", "https://github.com/username"),
)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
