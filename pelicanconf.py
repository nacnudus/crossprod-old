#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Duncan Garmonsway'
SITENAME = u'OPRE'
SITEURL = u'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# "elegant" theme
# -----------------------------------------------------------------------------#
# Required
THEME = '../pelican-themes/elegant'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'render_math']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'extra/favicon']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Optional from here on
RECENT_ARTICLES_COUNT = 10
# COMMENTS_INTRO = ''
# SITE_LICENSE ('')
# MAILCHIMP_FORM_ACTION ('string') # MailChimp
SITESUBTITLE = 'R for Operational Research'

LANDING_PAGE_ABOUT = {'title': 'I do data', 'details': 'My name is Duncan '
                      'Garmonsway.  I did data things in the New Zealand '
                      'government and now I study maths, statistics and '
                      'operations research at Victoria University of '
                      'Wellington.'}
# -----------------------------------------------------------------------------#

# Defaults
DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False

# Favicons
USE_SHORTCUT_ICONS = True
# # Other stuff to include in the web root
# EXTRA_PATH_METADATA = {
#     'extra/favicon/favicon.ico': {'path': 'favicon.ico'}
# }

# Blogroll
LINKS = (('R-bloggers', 'http://www.r-bloggers.com/'),
         ('StatsBlogs', 'www.statsblogs.com'),)

# Social
TWITTER_USERNAME = 'nacnudus'
SOCIAL = (('Github', 'https://github.com/nacnudus'),
          ('Twitter', 'https://twitter.com/nacnudus'),
          ('LinkedIn', 'https://nz.linkedin.com/in/duncangarmonsway'),)

