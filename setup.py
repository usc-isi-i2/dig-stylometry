from setuptools import setup, find_packages
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'name': 'digStylometry',
    'description': 'code to get signature to do stylometric analysis',
    'author': 'Rajagopal',
    'url': 'https://github.com/usc-isi-i2/dig-stylometry',
    'download_url': 'https://github.com/usc-isi-i2/dig-stylometry.git',
    'author_email': 'bojanapa@usc.edu',
    'install_requires': ['nose2',
                         'digSparkUtil',
                         'jq'],
    'version':'0.1.7',
    'packages': ['digStylometry'],
    'scripts': []
}

setup(**config)
