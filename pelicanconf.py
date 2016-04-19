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
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'render_math', 'assets'
           , 'neighbors', 'share_post', 'rmd_reader']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'figure', 'nzcrash_release_files']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Optional from here on
RECENT_ARTICLES_COUNT = 10
# SITE_LICENSE ('')
SITESUBTITLE = 'R for Operational Research'

# MailChimp
# Doesn't work with Github pages

# Landing page
# PROJECTS = [
#     {
#         'name': 'This blog',
#         'url':
#         'http://nacnudus.github.io/opre/',
#         'description': 'A blog about the R language and operations research'
#     },
# ]
LANDING_PAGE_ABOUT = {'title': 'About', 'details': 'My name is Duncan '
                      'Garmonsway.  I began doing data things in the New '
                      'Zealand government, and am now working in Glasgow, '
                      'Scotland, UK. I am an analyst who can code and who '
                      'knows undergrad statistics. This is my personal blog.'}

# Labels
SOCIAL_PROFILE_LABEL = u'Social'
RELATED_POSTS_LABEL = 'Keep Reading'
SHARE_POST_INTRO = 'Like this post? Share on:'
COMMENTS_INTRO = u'Please comment below'

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
SOCIAL = (('Github', 'https://github.com/nacnudus'),
          ('Twitter', 'https://twitter.com/nacnudus'),
          ('LinkedIn', 'https://nz.linkedin.com/in/duncangarmonsway'),
          # ('RSS', 'http://oncrashreboot.com/feeds/all.atom.xml'),
          )

# Search engine optimisation
SITE_DESCRIPTION = u'My name is Duncan Garmonsway \u2013 a analyst who can code and knows undergrad statistics. This is my personal blog.'

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
