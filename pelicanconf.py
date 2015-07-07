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

# Blogroll
LINKS = (('R-bloggers', 'http://www.r-bloggers.com/'),
         ('StatsBlogs', 'www.statsblogs.com'),)

# Social
TWITTER_USERNAME = 'nacnudus'
SOCIAL = (('Github', 'https://github.com/nacnudus'),
          ('Twitter', 'https://twitter.com/nacnudus'),
          ('LinkedIn', 'https://nz.linkedin.com/in/duncangarmonsway'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# "elegant" theme
# Required config for the "elegant" theme
THEME = '../pelican-themes/elegant'
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
# Optional config for the "elegant" theme
RECENT_ARTICLES_COUNT = 10
# COMMENTS_INTRO = ''
# SITE_LICENSE ('')
SITE_DESCRIPTION = 'About applying the R language to operational research.'
# EMAIL_SUBSCRIPTION_LABEL ('string') # MailChimp
# EMAIL_FIELD_PLACEHOLDER ('string') # MailChimp
# SUBSCRIBE_BUTTON_TITLE ('string') # MailChimp
# MAILCHIMP_FORM_ACTION ('string') # MailChimp
SITESUBTITLE = 'R for Operational Research'
LANDING_PAGE_ABOUT = {'I do data', 'My name is Duncan Garmonsway.  I did data things in the New Zealand government and now I study maths, statistics and operations research at Victoria University of Wellington.'}
# # PROJECTS ([{},...])
