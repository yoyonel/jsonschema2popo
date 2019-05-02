"""
TODO: refacto here !
On:
- packages dependencies
- use_scm
"""
from collections import defaultdict
from pathlib import Path

from setuptools import setup
import os
from os import path

here = os.path.abspath(os.path.dirname(__file__))

# read the contents of your README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requires = defaultdict(
    list,
    {
        p.stem: p.read_text().split()
        for p in Path('requirements').glob('*.pip')
    }
)

setup(
    name='jsonschema2popo',
    use_scm_version=True,
    description='Converts a JSON Schema to a Plain Old Python Object class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    url='https://github.com/yoyonel/jsonschema2popo',
    author=['ATTY Lionel', 'cruc.io'],
    author_email='yoyonel@hotmail.com',
    keywords='python json-schema code-generator',
    license='MIT License',
    python_requires='>=3.6',
    install_requires=requires['base'],
    setup_requires=requires['setup'],
    extras_require={
        'test': requires['test'],
        'develop': requires['test'] + requires['dev'],
        'docs': requires['docs']
    },
    packages=["jsonschema2popo"],
    package_data={"jsonschema2popo": ["_class.tmpl"]},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "jsonschema2popo=jsonschema2popo.jsonschema2popo:main"
        ]
    },
)
