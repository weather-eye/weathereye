#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['redis',
                'ansible',
                'django==4.1',
                'Click>=8.1.7',
                'celery>=4.0.0',
                'whitenoise>=6.7.0',
                'ansible-runner==2.4.0',]

test_requirements = [ ]

setup(
    author="Ian Edwards",
    author_email='ian@myacorn.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="WeatherEye Python Package and CLI",
    entry_points={
        'console_scripts': [
            'weathereye=weathereye.cli:main',
            'wx=weathereye.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='weathereye',
    name='weathereye',
    packages=find_packages(include=['weathereye', 'weathereye.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/isedwards/weathereye',
    version='0.1.0',
    zip_safe=False,
)
