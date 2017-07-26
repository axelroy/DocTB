#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MIP App Framework documentation build configuration file, created by
# sphinx-quickstart on Tue Feb  7 00:24:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax', 'sphinxcontrib.bibtex', 'sphinx_numfig']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Automated Machine Learning'
copyright = '2017, Axel Roy'
author = 'Axel Roy'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.1'
# The full version, including alpha/beta/rc tags.
release = '0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Marackerdoc'

# -- Options for LaTeX output ---------------------------------------------

# ADDITIONAL_PREAMBLE = """
# \input{preamble._tex}
# \usepackage{sphinx}
# """

latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize':
    'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize':
    '12pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': ADDITIONAL_PREAMBLE,
  #   'preamble': r'''
  #      \makeatletter
  #      \renewcommand{\maketitle}{
  #        \begin{titlepage}
  #
  # begin{center}
  # \large \textsc{\ifthenelse{\boolean{@french}}{Rapport de \@worktype}{\@worktype\ report}}}
  # ifthenelse{\boolean{@confidential}}{\\[2em]\textcolor{red}{\Large \textbf{\MakeUppercase{\confidentialname}}}}{}
  # end{center}
  # \vskip 60\p@
  # \begin{center}%
  #   {\Huge \@title \par}%
  #   \vskip 6em%
  #   {\large
  #    \lineskip .75em%
  #     \begin{tabular}[t]{l l}%
  #       {\small \authorname:} & \@author \\
  # 		{\small \professorname:} & \@professor \\
  # 		{\small \requestorname:} & \@requestor \\
  # 		{\small Date:} & \@date \\
  # 		{\small \versionname:} & {\small \@version}\\[1em]
  # 		%\@projectnumber
  #     \end{tabular} \hspace*{\fill}
  # 	%\@author \\[2em]
  # 	%\@date , version \@version
  # 	\par}%
  #     \vskip 1.5em%
  # \end{center}\par
  # \vfil\null
  # \end{titlepage}
  #        \end{titlepage}
  #      }
  #      \makeatother''',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'fontpkg':
    r'\setmainfont{Linux Libertine O}'
    r'\setsansfont{Linux Biolinum O}'
    r'\setmonofont[Scale=0.9]{Inconsolata}'
    r'\defaultfontfeatures{Scale=MatchLowercase,Mapping=tex-text,'
    r'Numbers=OldStyle,'
    r'Ligatures={Common,Rare,Discretionary,Historic}}',
    'fncychap':
    r'\usepackage[Bjornstrup]{fncychap}',
}

latex_show_urls = 'footnote'


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AutoML.tex', 'Rapport de projet AutoML', 'Axel Roy',
     'report'),
]

latex_additional_files = [
    'tex/preamble._tex'
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'AutoML', 'AutoML', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Automated Machine Learning', 'Rapport de projet du travail de Bachelor 17INF-TB225 -  Automated Machine Learning', author, 'Rapport de projet du travail de Bachelor 17INF-TB225 -  Automated Machine Learning',
     'Optimisation automatique du pipeline de Machine Learning dans le cadre du Human Brain Project SP8.', 'Machine Learning'),
]



 # latex_logo = 'images/ml_pipeline.png'
