import io
import json
import os
from setuptools import setup

# Package meta-data.
NAME = 'dash-gif-component'
URL = 'https://github.com/mbkupfer/dash-gif-component.git'
EMAIL = 'mbkupfer@gmail.com'
AUTHOR = 'Maxim Kupfer'


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Use package.json to grab details
with open(os.path.join('dash_gif_component', 'package.json')) as f:
    package = json.load(f)


package_name = package["name"].replace(" ", "_").replace("-", "_")
setup(
    name=NAME,
    version=package["version"],
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package['description'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['dash>=0.38']
)
