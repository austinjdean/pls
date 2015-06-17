#!/usr/bin/env python

import sys
import subprocess

query = ''

for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
	query += arg
	query += '+'

query = 'https://www.google.com/search?q=' + query

subprocess.call(["google-chrome-stable", query]) # TODO: make this call the user's favorite browser instead of forcing Chrome
