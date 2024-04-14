==========
WeatherEye
==========


.. image:: https://img.shields.io/pypi/v/weathereye.svg
        :target: https://pypi.python.org/pypi/weathereye

..
    .. image:: https://img.shields.io/travis/isedwards/weathereye.svg
            :target: https://travis-ci.com/isedwards/weathereye
    
    .. image:: https://readthedocs.org/projects/weathereye/badge/?version=latest
            :target: https://weathereye.readthedocs.io/en/latest/?version=latest
            :alt: Documentation Status


WeatherEye Python Package and Command Line Interface (CLI)

* Free software: MIT license
* Documentation: https://docs.weathereye.org

Install
-------

To install the most recent release from the Python Package Index, first install `pipx<https://pipx.pypa.io/stable/#install-pipx>`_

.. code-block::

    pipx install weathereye

To download and install the most recent updates from GitHub (note this installs all of WeatherEye's dependencies into your current environment):

.. code-block::

    git clone https://github.com/weather-eye/weathereye
    pip install -e weathereye


Features
--------

Currently the weathereye commandline tool is limited to:

* ``wx install surface`` - Install SURFACE CDMS

..
    Credits
    -------
    
    This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
    
    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage