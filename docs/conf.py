# -*- coding: utf-8 -*-
import os

import alagitpull

# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# package data
about = {}
with open("../libvcs/__about__.py") as fp:
    exec(fp.read(), about)

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    'alagitpull',
    'sphinx_issues',
]

releases_unstable_prehistory = True
releases_document_name = ["history"]
releases_issue_uri = "https://github.com/vcs-python/libvcs/issues/%s"
releases_release_uri = "https://github.com/vcs-python/libvcs/tree/v%s"

issues_github_path = about['__github__']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = about['__title__']
copyright = about['__copyright__']

version = '%s' % ('.'.join(about['__version__'].split('.'))[:2])
release = '%s' % (about['__version__'])

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme_path = [alagitpull.get_path()]
html_favicon = 'favicon.ico'
html_theme = 'alagitpull'
html_theme_options = {
    'logo': 'img/libvcs.svg',
    'github_user': 'vcs-python',
    'github_repo': 'libvcs',
    'github_type': 'star',
    'github_banner': True,
    'projects': alagitpull.projects,
    'project_name': about['__title__'],
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'more.html',
        'searchbox.html',
    ]
}

html_static_path = ['_static']
htmlhelp_basename = '%sdoc' % about['__title__']

alagitpull_internal_hosts = ['libvcs.git-pull.com', '0.0.0.0']
alagitpull_external_hosts_new_window = True


latex_documents = [
    (
        'index',
        '{0}.tex'.format(about['__package_name__']),
        '{0} Documentation'.format(about['__title__']),
        about['__author__'],
        'manual',
    )
]

man_pages = [
    (
        'index',
        about['__package_name__'],
        '{0} Documentation'.format(about['__title__']),
        about['__author__'],
        1,
    )
]

texinfo_documents = [
    (
        'index',
        '{0}'.format(about['__package_name__']),
        '{0} Documentation'.format(about['__title__']),
        about['__author__'],
        about['__package_name__'],
        about['__description__'],
        'Miscellaneous',
    )
]

intersphinx_mapping = {
    'py': ('https://docs.python.org/2', None),
    'pip': ('http://pip.readthedocs.io/en/latest/', None),
}
