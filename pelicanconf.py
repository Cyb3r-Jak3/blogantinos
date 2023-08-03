AUTHOR = 'Author'
SITENAME = 'blogantinos'
SITEURL = 'http://127.0.0.1:8000/'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

SUBTITLE = ' '
SUBTEXT = '''
<style>
  .image-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* max-width: 60 0px; */
  }

  .resized-image {
    width: 300px;
    height: auto;
    border-radius: 5%;
  }

  .text-container {
    margin-top: 20px;
  }
</style>

<div class="image-container">
  <a href="#">
    <img src="images/cycling.gif" alt="Welcome!" class="resized-image">
  </a>

  <div class="text-container">
    <h1>Code, Coffee, and Data Science stuff! (okay and a little bit more)</h1>
  </div>
</div>
'''

COPYRIGHT = '©2023'
PATH = 'content'
THEME = 'themes/Papyrus'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['search', 'neighbors', 'pelican-toc'] #'readtime'
STATIC_PATHS = [
    'images',
    'images/favicon.ico',
    'images/favicon-32x32.png',
    ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    }
DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'archives': 24,}

# Site search plugin
STORK_INPUT_OPTIONS = {
    'url_prefix': SITEURL
}
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"

# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widgets
SOCIAL = (
    ('github', 'https://github.com/KonstantinosTsoumas'),
    ('linkedin', 'https://www.linkedin.com/in/konstantinostsoumas'),
)

# Article share widgets
SHARE = (
    ("linkedin", "https://www.linkedin.com/in/konstantinostsoumas/"),
    ("github", "https://github.com/KonstantinosTsoumas/"),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
