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

To install the most recent release from the Python Package Index, first install `pipx<https://pipx.pypa.io/stable/#install-pipx>`_

.. code-block::

    pipx ensurepath

Ensure to run after installing pipx to make sure that the directory where pipx stores applications are included in your PATH. Make sure you close the terminal and reopen it for changes to take effect.

.. code-block::

    pipx install weathereye

To download and install the most recent updates from GitHub (note this installs all of WeatherEye's dependencies into your current environment):

.. code-block::

    git clone https://github.com/weather-eye/weathereye
    pip install -e weathereye


Features
--------

Currently, the weathereye command line tool is limited to:

* ``wx install surface`` - Install SURFACE CDMS

* ``wx install surface-remote`` - Install SURFACE CDMS on a remote machine


Usage
-----

1. **Before running any commands, activate the weathereye virtual environment created by pipx:**

* Find the virtual environment path: 
   Run ``pipx list`` which will show a path like ``path/to/venvs/weathereye``.

* Activate the environment: 
   ``source path/to/venvs/weathereye/bin/activate``

* Deactivate the environment: 
   ``deactivate``

2. **When installing SURFACE on remote machines you will be prompted to provide a hosts list:**

* Create a host list file:
    * Create a YAML file (``.yml`` extension) containing the hostnames or IP addresses of the remote machines.

* Populate host list file:
    * Each hostname or IP address should be on a separate line.

    * Example Host List (``hosts.yml``):

        .. code-block::
        
            username@xxx.xx.xxx.xxx
            xxx.xx.xxx.xxx

* Enter the absolute path to the file you created (e.g., ``/path/to/hosts.yml``)

..
    Credits
    -------
    
    This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.
    
    .. _Cookiecutter: https://github.com/audreyr/cookiecutter
    .. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
