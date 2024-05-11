"""Top-level package for WeatherEye."""

import os
import logging

logfile = os.path.dirname(__file__) + "/logs/app.log"

logging.basicConfig(level=logging.INFO, filename=logfile, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

__author__ = """Ian Edwards"""
__email__ = 'ian@myacorn.com'
__version__ = '0.1.0'
