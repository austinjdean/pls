#!/usr/bin/env python

import sys
import subprocess
import os
import re
import urllib2

# Global variables - _g suffix indicates global status

url_g = 'https://www.google.com/search?q=' # default to standard google search
dbf_g = False # debug flag - boolean variable to handle debug options

def printHelp():
    print 'Usage:\n'
    print '\tpls [options] [search terms]\n'
    print 'Options:\n'
    print '\t-c: open using Chrome\n'
    print '\t-f: open using Firefox\n'
    print '\t-l: I\'m Feeling Lucky\n'
    print '\t-s: search using Google Scholar\n'
    print '\t-i: search using Google Images\n'
    print '\t-m, --sass: increase sass - search using Let Me Google That For You\n'
    print '\t-d: debug flag - prints the URL that pls will open\n'
    print '\t-h, --help: display usage information and exit\n'
    print 'Notes:'
    print '\t- search terms do not need to be enclosed in quotes.'
    print '\t- any special characters (*, ", $, etc...) will be consumed by the shell before the script can even get its hands on them. To use these literal characters in a search query, escape them with \.'

def getQuery():
    '''
    Gets the query string that will be appended to the appropriate URL. 
    '''
    query = '' #The query to be returned

    #Build the query 
    for arg in sys.argv[1:]: # skip first argument in sys.argv because it's the name of the script
        if arg == '-c':
            browser = 'google-chrome'
        elif arg == '-f':
            browser = 'firefox'
        elif arg == '-d':
            global dbf_g
            dbf_g = True
        elif arg == '-i':
            pass # images
        elif arg == '-s':
            pass # scholar
        elif arg == '-m' or arg == '--sass':
            pass # LMGTFY
        elif arg == '-h' or arg == '--help':
            printHelp()
            exit(0)
        elif arg == '-l':
            pass # lucky
        else: # arg is just a word, add it to the query string
            query += arg
            query += '+'

    # thanks: http://stackoverflow.com/questions/15478127/remove-final-character-from-string-python
    query = query[:-1] # remove final '+' added by for loop
    return query

def determineURL(option):
    '''
    Sets global URL (e.g. to search Images, Scholar, LMGTFY, etc.) given the correcponsing flag.
    '''
    global url_g

    if option == '-l': # I'm Feeling Lucky
        req = urllib2.Request(url_g, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
        con = urllib2.urlopen(req).read() # get html source
        searchObj = re.search( r'<h3 class="r"><a href="(.*?)"', con) # get first occurrence of a result and capture its URL
        url_g = searchObj.group(1)

    elif option == '-s': # Scholar
        url_g = 'https://scholar.google.com/scholar?q='

    elif option == '-i': # Images
        baseURL = 'https://www.google.com'
        req = urllib2.Request(url_g, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
        con = urllib2.urlopen(req).read()
        searchObj = re.search( r'<a class="q qs" href="([^"]*)">Images</a>', con)
        imgHash = searchObj.group(1)
        imgHash = imgHash.replace('&amp;', '&')
        url_g = baseURL + imgHash

    elif option == '-m' or option == '--sass': # Let Me Google That For You
        url_g = 'http://www.lmgtfy.com/?q='

    # additional options here

def debugPrint(string):
    if dbf_g == 1:
        print string    

def main():
    query = ''
    browser = 'xdg-open' # system default browser - thanks: http://stackoverflow.com/questions/5116473/linux-command-to-open-URL-in-default-browser
    DEVNULL = open(os.devnull, 'w')

    query = getQuery()
    
    global url_g
    url_g += query # default to standard Google search

    if '-l' in sys.argv:
        determineURL('-l') # no need to assign to variable; this function sets the global variable
        # do not append query here; the purpose of -l is to access first link of results

    if '-s' in sys.argv:
        determineURL('-s')
        url_g += query

    if '-i' in sys.argv:
        determineURL('-i')

    if '-m' in sys.argv or '--sass' in sys.argv:
        determineURL('-m')
        url_g += query

    debugPrint(url_g)

    subprocess.call([browser, url_g], stdout=DEVNULL, stderr=subprocess.STDOUT) # shhhh - redirect browser output to /dev/null
    # thanks: http://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7

if __name__ == '__main__':
    main()
