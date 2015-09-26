#!/usr/bin/python

import os
# os.environ['PYTHON_EGG_CACHE'] = '/var/www/LeagueAPIChallenge/python-eggs' 

activate_this = '/var/www/airtalk/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/airtalk')
sys.path.append('/var/www/airtalk')

from hello import app as application
