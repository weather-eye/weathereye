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


Supported Operating Systems
---------------------------
Linux

* ``Ubuntu 22.04``


Install
-------

Update and Upgrade Packages

.. code-block::

    sudo apt update
    sudo apt upgrade

Install pipx and reload the shell

.. code-block::

    sudo apt install pipx -y; pipx ensurepath; exec "$SHELL" -l

Install development version of weathereye

.. code-block::

    cd ~
    git clone https://github.com/weather-eye/weathereye
    pipx install ~/weathereye

Run weathereye installer

.. code-block::

    wx install

Features
--------

Currently, the weathereye command line tool is limited to:

* ``wx --help`` - List available available commands

* ``wx install`` - Launches a web application to select which ``weathereye`` related app to install and configure environment variables


Usage
-----

1. **Enable SSH connections for remote machines:**

* To download SURFACE on remote machines, ensure that the remote machines can be accessed via SSH.

..
    Credits
    -------
    
    This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
    
    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
