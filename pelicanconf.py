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

# labels
SOCIAL_PROFILE_LABEL = u'Stay in Touch'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'

# -----------------------------------------------------------------------------#

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = False
TYPOGRIFY = True
DEFAULT_PAGINATION = False
ARTICLE_URL = u'{slug}'
PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}.html'

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
# FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
SOCIAL = (('Github', 'https://github.com/nacnudus'),
          ('Twitter', 'https://twitter.com/nacnudus'),
          ('LinkedIn', 'https://nz.linkedin.com/in/duncangarmonsway'),)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
