#!/home/fuzzyklein/python/bin/python3
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
print('<!DOCTYPE html>')

# Should make the logging module work or else develop a custom Logger class.
if __debug__:
    LOGFILE = 'pycgi.log'
    LOG = Path(LOGFILE)
    # Clear the log file
    LOG.write_text("")

    def log(s):
        """Append the str s to the log file."""
        with LOG.open(mode='a') as f:
            f.write(s + '\n')

    log(f"Log file {LOGFILE} initialized: {dt.now()}")

KEYS = ENV.keys()
QS = "QUERY_STRING"
CGI_MODE = QS in KEYS
qs = "home"

if CGI_MODE:
    qs = ENV[QS]
elif len(sys.argv) > 1:
    qs = sys.argv[1]

# print(f'{qs}')

BR = '<br/>'
CONTENTS = '<div id="contents"></div>'
KEY = qs.upper()

# page.html supplies the outer shell for the HTML page output
tree = ET.parse('page.html')
html = tree.getroot() # HTML element

if __debug__:
    log("Root element of page.html:")
    log("")
    log(ET.tostring(html, encoding='unicode', method='html'))

try:
    head = html.find('head')
    body = html.find('body')
    title = head.find('title')
    cp = CP()
    cp.read('metas.ini')
    title.text = cp[KEY]['TITLE']
except:
    log("Error setting the title tag.")

if __debug__:
    log("Root element of page.html with title tag:")
    log("")
    log(ET.tostring(html, encoding='unicode', method='html'))

# If memory serves, this still causes text output to the HTML
# output.find('./head/meta[@name="description"]').text = cp[KEY]['DESCRIPTION']

navtree = ET.parse('nav.html')
menus = navtree.getroot()
nav = menus.find('div[@id="navbar"]')
socials = menus.find('div[@id="socials"]')
# Read the configuration file for social media icons.
cp = CP()
cp.read('social.ini')

for key in [k for k in cp.keys() if k != 'DEFAULT']:
    if __debug__:
        log(f'Searching for cp[{key}]["LINK"]...')
    LINK = cp[key]['LINK']
    if LINK:
        ID = key.lower()
        p = ID + '.png'
        TIP = cp[key]['tip']
        attrib = {'href' : LINK, 'id' : ID, 'target' : '_blank',
              'title' : TIP 
             }
        a = ET.Element('a', attrib=attrib)
        a.append(ET.Element('img', attrib={'src' : p}))
        socials.append(a)
nav.append(socials)

# Read the configuration file for the links in the Navigation bar.
cp = CP()
cp.read('metas.ini')

# Add a link for each section of the nav configuration file.
for k in cp.keys():
    if k != 'DEFAULT':
        TITLE = cp[k]['TITLE']
        k = k.lower()
        attrib = {'id' : k,
                  'href' : f'index.cgi?{k}',
                  'title' : TITLE
                 }
        if k == qs:
            attrib['class'] = 'active'
        e = ET.Element('a', attrib=attrib)
        strong = ET.Element('strong')
        strong.text = k.title()
        e.append(strong)
        nav.append(e)

# menus.append(nav)
body.append(menus)

if __debug__:
    log("Output element with navigation bar:")
    log("")
    log(ET.tostring(html, encoding='unicode', method='html'))

contents = ET.fromstring(CONTENTS)

# Find the local file whose stem matches the query string.
P = None
for f in ls():
    if Path(f).stem == qs:
        P = Path(f)
if not P:
    log(f"ERROR! Can't find file matching: {qs}")
    attrib = { 'class' : 'center',
               'src' : 'black-construction.jpg'
             }
    e = ET.Element('img', attrib=attrib)
    contents.append(e)
    body.append(contents)

# Process the file according to its extension.
elif P.suffix == '.html':
    body.append(ET.parse(str(P.resolve())).getroot())
elif P.suffix == '.py':
    params = ["python3"]
    if not __debug__:
        params.append("-OO")
    params.append(P.name)
    body.append(ET.fromstring(check_output(params, encoding='utf-8')))
elif P.suffix == '.md':
    body.append(ET.fromstring(md(P.resolve().read_text())))

# output.append(body)
# print('<!DOCTYPE html>')
print(ET.tostring(html, encoding='unicode', method='html'))

if __debug__:
    log(f"Execution complete: {dt.now()}")
