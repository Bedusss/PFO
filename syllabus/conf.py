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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LSINC1102'
copyright = '2020, Olivier Bonaventure'
author = 'Olivier Bonaventure'

# The full version, including alpha/beta/rc tags
release = '2020'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinxcontrib.spelling',
               'sphinxcontrib.tikz',
               'sphinxcontrib.video',
]

#               'matplotlib.sphinxext.only_directives',
#               'matplotlib.sphinxext.plot_directive',


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '._*.rst']

master_doc = 'index'

# sphinx

numfig=True  # numérotation des figures

# Spelling checker


#spelling
spelling_lang='fr'
spelling_word_list_filename='dict.txt'
tokenize_lang='fr'
spelling_ignore_acronyms=True
spelling_show_suggestions=True

# latex

latex_elements = {
    'preamble': r'''
\pgfplotsset{compat=1.16}
\usepackage{circuitikz}
'''
}
# tikz

tikz_tikzlibraries = "circuits.logic.US,positioning,calc,quotes,backgrounds,matrix"
tikz_proc_suite = 'ImageMagick'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
