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
import re
import sys

import recommonmark  # noqa: F401
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('../pyclesperanto_prototype/'))
from pyclesperanto_prototype import __version__

import pyclesperanto_prototype as cle
all = ""
for key in cle.operations():
    all = all + key + ", "

filename = "index.rst"
index = open(filename).readlines()
new_index = []
for line in index:
    if ":members:" in line:
        line = "   :members: " + all + "\n"
    new_index = new_index + [line]

result = open(filename, "w+")
result.writelines(new_index)
result.close()

# -- Project information -----------------------------------------------------

project = 'pyclesperanto_prototype'
copyright = '2020, Robert Haase'
author = 'Robert Haase'

release = __version__
version = __version__
CONFDIR = os.path.dirname(__file__)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# intersphinx allows us to link directly to other repos sphinxdocs.
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
}

#
html_theme = 'sphinx_rtd_theme'
html_logo = "images/cle_logo.png"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# app setup hook
github_doc_root = 'https://github.com/clesperanto/pyclesperanto_prototype/tree/master/docs/'


def setup(app):
    app.add_config_value(
        'recommonmark_config',
        {
            'url_resolver': lambda url: github_doc_root + url,
            'enable_auto_toc_tree': True,
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
        },
        True,
    )
    app.add_transform(AutoStructify)