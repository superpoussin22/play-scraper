import re
from setuptools import setup


with open('play_scraper/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='play_scraper',
    version=version,
    description='Google Play Store application scraper',
    long_description='Web scraper to retrieve application details from '
    'the Google Play Store',
    url='https://github.com/danieliu/play-scraper',
    author='Daniel Liu',
    author_email='idaniel.liu@gmail.com',
    packages=['play_scraper'],
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'beautifulsoup4>=4.4.1',
        'grequests>=0.3.0',
        'lxml>=3.6.0',
        'requests>=2.9.1',
    ],
)
