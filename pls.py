#!/usr/bin/env python

import sys, subprocess, os, re, urllib2, argparse, random, textwrap

# Global variables - _g suffix indicates global status
url_g = 'https://www.google.com/search?q=' # default to standard google search
browser_g = 'xdg-open' # use system default as default browser
parser_g = argparse.ArgumentParser(epilog='Special characters (*, ", $, etc.) must be escaped using \, and search terms do not need to be enclosed in quotes.') # global argument parser

# register arguments with the parser
def initParser():
	'''
	Initializes the parser to accept all defined arguments. Future options should be registered here.
	'''
	browserArgGroup = parser_g.add_mutually_exclusive_group()
	flagArgGroup = parser_g.add_mutually_exclusive_group()

	parser_g.add_argument(
			'terms',
			help='Search terms to be passed to Google',
			nargs='*')
	parser_g.add_argument(
			'-d',
			'--debug',
			help='Print the target URL instead of opening it',
			action='store_true')
	parser_g.add_argument(
			'-F',
			'--force',
			help='Force pls to attempt to open in browser',
			action='store_true')
	browserArgGroup.add_argument(
			'-c',
			'--chrome',
			help='Open using Chrome',
			action='store_true')
	browserArgGroup.add_argument(
			'-f',
			'--firefox',
			help='Open using Firefox',
			action='store_true')
	flagArgGroup.add_argument(
			'-t',
			'--text',
			help='Display results in the terminal instead of showing them in browser',
			action='store_true')
	flagArgGroup.add_argument(
			'-w',
			'--word',
			help='Show syllable segmentation, pronunciation, and definition of WORD in the terminal',
			nargs='*')
	flagArgGroup.add_argument(
			'-l',
			'--lucky',
			help='I\'m Feeling Lucky',
			action='store_true')
	flagArgGroup.add_argument(
			'-i',
			'--images',
			help='Search using Google Images',
			action='store_true')
	flagArgGroup.add_argument(
			'-S',
			'--scholar',
			help='Search using Google Scholar',
			action='store_true')
	flagArgGroup.add_argument(
			'-n',
			'--news',
			help='Search using Google News',
			action='store_true')
	flagArgGroup.add_argument(
			'-m',
			'--maps',
			help='Search using Google Maps',
			action='store_true')
	flagArgGroup.add_argument(
			'-v',
			'--video',
			help='Search using Google Video',
			action='store_true')
	flagArgGroup.add_argument(
			'-s',
			'--site',
			help='Search a specific website')
	flagArgGroup.add_argument(
			'-L',
			'--sass',
			help='Increase sass - open "Let Me Google That For You" URL',
			action='store_true')
	flagArgGroup.add_argument(
			'-r',
			'--simpsons',
			help='Open a randomly selected Simpsons episode',
			action='store_true')
	flagArgGroup.add_argument(
			'-x',
			'--xkcd',
			help='Open a randomly selected xkcd comic',
			action='store_true')

def which(program): # thanks: http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
	'''
	Function to determine whether a program exists
	'''
	def is_exe(fpath):
		return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			path = path.strip('"')
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None

def determineBrowser(argList):
	'''
	Sets global browser variable; the default value (xdg-open) is initialized with the global variable, so it is not specified here.
	'''
	global browser_g
	if argList.chrome == True:
		if which('google-chrome'):
			browser_g = 'google-chrome'
		else:
			print 'Google Chrome is not installed.'
			exit(1)

	elif argList.firefox == True:
		if which('firefox'):
			browser_g = 'firefox'
		else:
			print 'Firefox is not installed.'
			exit(1)

def getQuery():
	'''
	Gets the query string that will be appended to the appropriate URL.
	'''
	query = '+'.join(parser_g.parse_args().terms) # thanks: https://www.reddit.com/r/Drexel/comments/3hv00r/psa_cs_students_im_making_something_i_hope_youll/cubkrrs
	query = query.strip()
	query = query.replace(' ', '+') # if user used quotes, account for spaces
	return query

def internetOn(): # thanks: http://stackoverflow.com/questions/3764291/checking-network-connection
	try:
		response = urllib2.urlopen('http://google.com/', timeout = 1)
		return True
	except urllib2.URLError as err: pass
	return False

def exitIfNoInternet():
	if not internetOn():
		print 'Problem connecting to the internet.'
		exit(64) # exit code 64 means machine is not on the network

def getSource(url):
	# thanks: http://stackoverflow.com/questions/30580639/cant-get-python-to-download-webpage-source-code-browser-version-not-supported
	req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
	source = urllib2.urlopen(req).read() # get html source
	return source

def determineURL(argList):
	'''
	Sets global URL (e.g. to search Images, Scholar, LMGTFY, etc.) given the corresponding flag.
	'''
	global url_g

	exitIfNoInternet()

	query = getQuery() # query to be appended to URL in some cases

	if argList.scholar:
		url_g = 'https://scholar.google.com/scholar?q=' + query
		# append query here to show Google results page with given query

	elif argList.lucky:
		url_g += query
		source = getSource(url_g)
		searchObj = re.search( r'<h3 class="r"><a href="(.*?)"', source) # get first occurrence of a result and capture its URL

		if not searchObj:
			print 'Warning: no luck finding links from which to grab the first.'

		else:
			url_g = searchObj.group(1)
		# do not append query here; the purpose of -l is to access first link of results

	elif argList.images:
		url_g = 'https://www.google.com/search?tbm=isch&q=' + query
		# append query here to display image results with given query

	elif argList.sass:
		url_g = 'http://www.lmgtfy.com/?q=' + query
		# append query here to pass search terms to LMGTFY

	elif argList.simpsons:
		seasonSelect = 'http://projectfreetv.so/free/the-simpsons/'
		source = getSource(seasonSelect)
		searchObj = re.findall( r'<a href="(http://projectfreetv.so/free/the-simpsons/the-simpsons-season-\d+/)" ?>', source)
		seasonURL = random.choice(searchObj)

		episodeSelect = seasonURL
		source = getSource(episodeSelect)
		searchObj = re.findall( r'<a href="(http://projectfreetv.so/the-simpsons-season-\d+-episode-\d+/)">', source)
		episodeURL = random.choice(searchObj)

		url_g = episodeURL

	elif argList.xkcd:
		# url_g = 'https://xkcd.com/4/' # guaranteed to be random
		url_g = 'http://c.xkcd.com/random/comic/'

	elif argList.news:
		url_g = 'https://www.google.com/search?tbm=nws&q=' + query
		# append query here to display news results with given query

	elif argList.video:
		url_g = 'https://www.google.com/#tbm=vid&q=' + query

	elif argList.site:
		query += '+site:' + argList.site
		url_g += query

	elif argList.maps:
		url_g = 'https://www.google.com/maps?q=' + query

	elif argList.text:
		url_g += query
		source = getSource(url_g)
		searchObj =  re.findall( r'<h3 class="r"><a href="(.*?)"[^>]*>(.*?)</a>', source) # get all occurrences of a result and capture URL and link title
		for result in searchObj:
			print result[1]
			print result[0]
			print

	elif argList.word: # todo: account for multiple definitions, such as "shoot"
		url_g += 'define+'
		url_g += '+'.join(argList.word)
		source = getSource(url_g)

		try: # isolate syllables and pronunciation becuase it's okay if we don't have those. Only fail for real if the definition is missing.
			try:
				syllables = re.search( r'<span data-dobid="hdw">(.*?)</span>', source)
				pronunciation = re.search( r'<span class="lr_dct_ph"><span>(.*?)</span>', source)
			except Exception, e:
				pass
			definition = re.search( r'(<span class="_Tgc">(.*?)</span><span)|(data-dobid="dfn"><span>(.*?)</span></div>)', source)

			try:
				syllables = syllables.group(1)
				pronunciation = pronunciation.group(1)
			except Exception, e:
				pass

			if definition.group(4):
				definition = definition.group(4)
			elif definition.group(2):
				definition = definition.group(2)

			definition = re.sub(r'<[^>]*>', '', definition) # remove formatting tags

			try:
				if syllables:
					print syllables
				if pronunciation:
					print pronunciation
			except Exception, e:
				pass

			print textwrap.fill(definition)

		except Exception, e:
			errorMessage = 'Couldn\'t find definition for "' + ' '.join(argList.word) + '."'
			print textwrap.fill(errorMessage)
			exit(1)

	# additional options here

	else: # default to standard Google search
		url_g += query

def debugPrint(string):
	if parser_g.parse_args().debug == True: # check arguments for -d flag
		print string

def main():
	'''
	Driver function for pls
	'''
	global url_g
	DEVNULL = open(os.devnull, 'w')

	initParser()
	determineBrowser(parser_g.parse_args())
	determineURL(parser_g.parse_args())
	# url_g = url_g.replace(' ', '+') # if user used quotes, account for spaces (line shouldn't be encessary, but I'm leaving it in case we run into trouble)
	debugPrint(url_g)

	if not (parser_g.parse_args().text or parser_g.parse_args().debug or parser_g.parse_args().word):
		if not parser_g.parse_args().force:
			try:
				if os.environ['SSH_CLIENT'] or os.environ['SSH_TTY']:
					print 'pls thinks it\'s over ssh right now. Try:'
					print '-F to force pls to attempt to open in browser (might hang terminal)'
					print '-d to print the URL pls would access instead of opening it'
					print '-t to display Google results in the terminal'
					print '-h for help'
					print 'If you\'re not over ssh, send expletives to austinjdean@gmail.com,'
					print 'or submit an issue: https://github.com/austinjdean/pls/issues'
					exit(2)
			except Exception, e: # not over ssh
				pass

		subprocess.call([browser_g, url_g], stdout=DEVNULL, stderr=subprocess.STDOUT) # shhhh - redirect browser output to /dev/null
		# thanks: http://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt: # thanks: http://stackoverflow.com/a/21144662/2929868
		print 'Exiting by user request.'
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
