#!/usr/bin/env python
"""
Django Admin App Bookmark

GitHub: https://github.com/kostyachum/django-admin-app-bookmark

Started and maintaned by Kostiantyn Chumachenko (https://github.com/kostyachum)


License: MIT (see LICENSE.md for details).
"""
from setuptools import setup

__version__, __version_info__ = '1.0.0', (1, 0, 0, 'final', 0)

# Get development Status for classifiers
dev_status_map = {
    'dev':   '2 - Pre-Alpha',
    'alpha': '3 - Alpha',
    'beta':  '4 - Beta',
    'rc':    '4 - Beta',
    'final': '5 - Production/Stable'
}
DEVSTATUS = dev_status_map[__version_info__[3]]

with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-admin-app-bookmark',
    version=__version__,
    url='https://github.com/kostyachum/django-admin-app-bookmark',
    project_urls={
        'Documentation': 'https://github.com/kostyachum/django-admin-app-bookmark/',
        'GitHub Project': 'https://github.com/kostyachum/django-admin-app-bookmark/',
        'Issue Tracker': 'https://github.com/kostyachum/django-admin-app-bookmark/issues'
    },
    description='Bookmarks for apps in django admin for better navigation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kostiantyn Chumachenko ',
    author_email='kostyachum@gmail.com',
    maintainer='Kostiantyn Chumachenko',
    maintainer_email='kostaychum@gmail.com',
    license='MIT License',
    packages=[
        'app_bookmarks',
        'app_bookmarks.migrations',
    ],
    include_package_data=True,
    package_data={'app_bookmarks': ['templates/*/*', 'static/*.*', 'static/**/*.*', 'static/**/**/*.*']},
    python_requires='>=3.6',
    install_requires=["Django>=3;python_version<'3.10'"],
    classifiers=[
        'Development Status :: %s' % DEVSTATUS,
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',        
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
