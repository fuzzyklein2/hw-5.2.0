#!/home/fuzzy/python-3.13.2/bin/python3.13
"""index.cgi

   Use an ElementTree to generate the HTML output instead of `print`.
"""
# title, description, and possibly keywords, etc. for each page
# are stored in a configuration file.
from configparser import ConfigParser as CP
from datetime import datetime as dt, timedelta as td
from getpass import getuser
from http import cookies
# import logging
# The query string is stored as an environment variable.
from os import environ as ENV, listdir as ls
from pathlib import Path
from subprocess import check_output
import sys
# The page.html file is a shell of the elements common to each page.
import xml.etree.ElementTree as ET

# The initial output of any CGI script is mandatory.
print('Content-Type: text/html\n')
print('<code>My script output goes here...</code>')

