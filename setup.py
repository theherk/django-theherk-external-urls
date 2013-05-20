import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-theherk-external-urls',
    version='1.1',
    packages=['menu_external_urls'],
    include_package_data=True,
    license='see file LICENSE',
    description='Django CMS plugin to allowing using external urls in the menu system.',
    long_description=read('README.md'),
    url='https://github.com/theherk/django-theherk-external-urls',
    author='Adam Sherwood',
    author_email='theherk@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
