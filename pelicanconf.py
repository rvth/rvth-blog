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
USER_LOGO_URL = "https://i.imgur.com/nlZmXCu.png"

THEME = "voce"

LOAD_CONTENT_CACHE = False
SLUGIFY_SOURCE = 'basename'


EXTRA_PATH_METADATA = {
    'files/favicon.ico': {'path': 'favicon.ico'},
    'files/robots.txt': {'path': 'robots.txt'},
}

#Theme specific
GOOGLE_ANALYTICS_ID = "UA-173020538-1"
GOOGLE_ANALYTICS_PROP = "rvth.blog"
TAGLINE = "Site Tagline"
MANGLE_EMAILS = False
GLOBAL_KEYWORDS = ("keywords",)


SOCIAL = (
    ("Twitter", "https://twitter.com/rvtheverett"),
    ("GitHub", "https://github.com/rvth"),
    ("Linkedin", "https://www.linkedin.com/in/ruth-everett-b01a6213b/"),
)

# Blogroll
LINKS = (("Home", "https://rvth.blog"),
         ("About", "/pages/about-me.html"),
         ("Ember", "/pages/ember.html"),
         ("Learning Log", "/pages/learning-log.html"),
         ('Python.org', 'http://python.org/'))

DEFAULT_PAGINATION = 10

RELATIVE_URLS = True
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = [".git"]

STATIC_PATHS = ['images']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 50

ARCHIVES_URL = "archives.html"
ARCHIVES_SAVE_AS = 'archives.html'
ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
TAGS_URL = 'tag/{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
