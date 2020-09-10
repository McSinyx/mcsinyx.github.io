# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
project = '/home/cnx'
copyright = '2018-2020, Nguyễn Gia Phong'
author = 'Nguyễn Gia Phong'

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.
extensions = ['sphinx.ext.extlinks', 'sphinx.ext.githubpages']
extlinks = {'pip': ('https://github.com/pypa/pip/pull/%s', 'GH-'),
            'github': ('https://github.com/%s', '@')}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Options for HTML output
html_theme = 'alabaster'
html_theme_options = {'fixed_sidebar': True,
                      'donate_url': 'https://liberapay.com/McSinyx'}

html_title = 'Raphael McSinyx'
html_logo = 'CnX.png'
html_favicon = 'favicon.ico'
html_css_files = ['fab.css']
html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory.  They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ['_static']
