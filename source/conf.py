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
templates_path = ['templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Options for HTML output
html_theme = 'furo'
css_variables = {'color-brand-primary': '#436e58',
                 'color-brand-content': '#436e58'}
html_theme_options = {'dark_css_variables': css_variables,
                      'light_css_variables': css_variables,
                      'sidebar_hide_name': True}

html_title = 'Raphael McSinyx'
html_logo = 'CnX.png'
html_favicon = 'favicon.ico'
html_show_copyright = False

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory.  They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ['static']
html_css_files = ['fab.css']
html_additional_pages = {'start': 'start.html'}
