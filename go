#!/usr/bin/env python

import sys
import subprocess
import time

query = ''
browser = "google-chrome-stable"
browserFlag = 0

for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
	if arg == "-b":
		browserFlag = 1
	elif browserFlag == 1:
		if arg == "firefox":
			browser = "firefox"
		browserFlag = 0
	else:
		query += arg
		query += '+'

query = 'https://www.google.com/search?q=' + query

subprocess.call([browser, query]) # TODO: make this call the user's favorite browser instead of forcing Chrome
