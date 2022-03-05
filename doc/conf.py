# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import datetime
import sys

import cofi

sys.path.insert(0, os.path.abspath("../cofi"))


# -- Project information -----------------------------------------------------

project = "CoFI"
copyright = f"{datetime.date.today().year}, InLab"
version = cofi.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
pygments_style = "default"
add_function_parentheses = False

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = True
numpydoc_show_class_members = False

# Disable including boostrap CSS for sphinx_panels since it's already included
# with sphinx-book-theme
panels_add_bootstrap_css = False
panels_css_variables = {
    "tabs-color-label-inactive": "hsla(231, 99%, 66%, 0.5)",
}


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# html_permalinks_icon = '§'
html_title = f'{project} <span class="project-version">{version}</span>'
html_short_title = project
html_logo = '_static/cofi-logo-thumbnail.jpg'
html_favicon = '_static/inlab_logo_60px.png'

html_theme = "sphinx_book_theme"
html_theme_options = {
    'launch_buttons': {
        'notebook_interface': 'classic',
        'inlab_url': 'http://www.inlab.edu.au/'
    }, 
    'path_to_docs': 'doc',
    'repository_url': 'https://github.com/inlab-geo/cofi',
    'repository_branch': 'main',
    'extra_footer': '',
    'home_page_in_toc': False,
    'use_repository_button': True,
    'use_edit_page_button': True,
    'use_issues_button': True
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["default.css"]


# -- Cutomised variables ------------------------------------------------------
rst_epilog = """
.. _repository: https://github.com/inlab-geo/cofi
.. _Slack: inlab-geo.slack.com
"""
