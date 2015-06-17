#!/usr/bin/env python

import sys
import subprocess
import time

query = ''

for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
	query += arg
	query += '+'

query = 'https://www.google.com/search?q=' + query

subprocess.call(["xdg-open", query]) # xdg-open uses system default browser
time.sleep(.3) # wait .3 seconds - necessary because chrome prints a message that looks like it hangs the terminal. Waiting allows that message to print before giving the prompt back to the user.
# there may be a much better solution for this, but this is a nice band-aid for now.
