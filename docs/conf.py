import datetime
import os
import sys

from sphinx_gallery.sorting import ExplicitOrder
from sphinx_gallery.sorting import NumberOfCodeLinesSortKey


sys.path.insert(0, os.path.abspath("../"))
import sparsereg

project = "Sparsereg"
copyright = "{}, Markus Quade".format(datetime.datetime.now().year)
author = "Markus Quade"
version = release = sparsereg.__version__

master_doc = "index"

extensions = [
    "sphinx.ext.mathjax",
    "sphinxcontrib.apidoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "sphinx_gallery.gen_gallery",
]


apidoc_module_dir = "../sparsereg"
apidoc_excluded_paths = ["tests"]

autodoc_default_flags = ["members"]
autodoc_member_order = "bysource"
autoclass_content = "init"

language = None

exclude_patterns = ["_build"]
pygments_style = "sphinx"

add_module_names = True
add_function_parentheses = False
todo_include_todos = True

html_theme = "sphinx_rtd_theme"
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

default_role = "any"

sphinx_gallery_conf = {
    "examples_dirs": "../examples",  # path to your example scripts
    "gallery_dirs": "examples",  # path where to save gallery generated examples
    "subsection_order": ExplicitOrder(["../examples/abstract", "../examples/concrete"]),
    "within_subsection_order": NumberOfCodeLinesSortKey,
    "filename_pattern": "/*.py",
    "ignore_pattern": r"__init__\.py",
    # "show_memory": True,
}
