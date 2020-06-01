# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

if not path.exists(path.join(here, 'src/ToJyutping/jyut6ping3.simple.dict.yaml')):
	raise Exception('Please run preprocess.py first.')

with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

with open(path.join(here, 'src/ToJyutping/version.py')) as f:
	exec(f.read())

setup(
	name='ToJyutping',
	version=__version__,
	description='粵語拼音自動標註工具 | Cantonese Pronunciation Automatic Labeling Tool',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/sgalal/to-jyutping',
	author='sgalal',
	author_email='ayaka@mail.shn.hk',
	license='Other',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Text Processing :: Linguistic',
		'Natural Language :: Cantonese',
		'Natural Language :: Chinese (Simplified)',
		'Natural Language :: Chinese (Traditional)',
		'License :: Other/Proprietary License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9'
	],
	keywords='chinese cantonese nlp natural-language-processing',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	package_data={
		'ToJyutping': ['jyut6ping3.simple.dict.yaml'],
	},
	include_package_data=True,
	python_requires='>=3.5, <4',
	install_requires=['pygtrie', 'opencc!=1.1.1'],
	entry_points={},
	project_urls={
		'Bug Reports': 'https://github.com/sgalal/to-jyutping/issues',
		'Source': 'https://github.com/sgalal/to-jyutping',
	},
	zip_safe=False
)
