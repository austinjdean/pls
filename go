#!/usr/bin/env python

import sys
import subprocess
import os

query = ''
browser = "xdg-open" # system default browser
DEVNULL = open(os.devnull, 'w')

for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
	if arg == "-c":
		browser = "google-chrome"
	elif arg == "-f":
		browser = "firefox"
	else:
		query += arg
		query += '+'

query = 'https://www.google.com/search?q=' + query

subprocess.call([browser, query], stdout=DEVNULL, stderr=subprocess.STDOUT) # shhhh - redirect browser output to /dev/null
