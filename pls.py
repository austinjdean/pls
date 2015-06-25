#!/usr/bin/env python

import sys
import subprocess
import os
import re
import urllib2
import argparse

# Global variables - _g suffix indicates global status

url_g = 'https://www.google.com/search?q=' # default to standard google search
parser_g = argparse.ArgumentParser() # global argument parser
browser_g = 'xdg-open' # use system default as default browser

# utility functions
def trueCount(boolList):
    count = 0 # number of true items in the list
    for current in boolList:
        if current == True:
            count += 1
    return count

def debugPrint(string):
    if parser_g.parse_args().d == True: # check arguments for -d flag
        print string

# register arguments with the parser
def initParser():
    '''
    Initializes the parser to accept all defined arguments. Future options should be registered here.
    '''
    parser_g.add_argument(
            'terms',
            nargs='*')
    parser_g.add_argument(
            '-c',
            help='open using Chrome',
            action='store_true')
    parser_g.add_argument(
            '-f',
            help='open using Firefox',
            action='store_true')
    parser_g.add_argument(
            '-s',
            help='search using Google Scholar',
            action='store_true')
    parser_g.add_argument(
            '-l',
            help='I\'m Feeling Lucky',
            action='store_true')
    parser_g.add_argument(
            '-i',
            help='search using Google Images',
            action='store_true')
    parser_g.add_argument(
            '-m',
            help='increase sass - search using Let Me Google That For You',
            action='store_true')
    parser_g.add_argument(
            '-d',
            help='debug flag - prints the URL that pls will open',
            action='store_true')

def validateArgs():
    '''
    Ensures there are no conflicts with the given arguments, and provides warning and error messages, and exits when need be.
    '''
    args = parser_g.parse_args()

    # Group conflicting options
    # conflicting groups:
    # [c,f] [s,l,i,m]
    # If one argument in a given set is chosen, no others from that set may be chosen.
    browserArgs = []
    browserArgs.append(args.c)
    browserArgs.append(args.f)

    flagArgs = []
    flagArgs.append(args.s)
    flagArgs.append(args.l)
    flagArgs.append(args.i)
    flagArgs.append(args.m)

    browserTrueCount = trueCount(browserArgs)
    flagTrueCount = trueCount(flagArgs)

    if flagTrueCount > 1:
        # give error message that only one flag of the set [s,l,i,m] can be used at once
        print 'Only one flag from the option set [-s,-l,-i,-m] may be used at once.'
        exit(1)

    if browserTrueCount > 1:
        # give warning message that only one browser can be specified and use system default
        print 'Warning: multiple browsers specified. Using system default browser...'
        browser_g = 'xdg-open'

def determineBrowser(argList):
    '''
    Sets global browser variable; the default value (xdg-open) is initialized with the global variable, so it is not specified here.
    '''
    global browser_g
    if argList.c == True:
        browser_g = 'google-chrome'

    elif argList.f == True:
        browser_g = 'firefox'

def getQuery():
    '''
    Gets the query string that will be appended to the appropriate URL. 
    '''
    global parser_g
    query = ''
    terms = parser_g.parse_args().terms
    for term in terms:
        query += term
        query += '+'
    query = query[:-1] # remove final '+' added by for loop
    return query

def determineURL(argList):
    '''
    Sets global URL (e.g. to search Images, Scholar, LMGTFY, etc.) given the corresponding flag.
    '''
    global url_g
    query = getQuery() # query to be appended to URL in some cases

    url_g += query # default to standard Google search

    if argList.s == True: # Scholar
        url_g = 'https://scholar.google.com/scholar?q='
        url_g += query
        # append query here to show Google results page with given query

    elif argList.l == True: # I'm Feeling Lucky
        req = urllib2.Request(url_g, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
        con = urllib2.urlopen(req).read() # get html source
        searchObj = re.search( r'<h3 class="r"><a href="(.*?)"', con) # get first occurrence of a result and capture its URL

        if not searchObj:
            print 'Warning: no search terms detected. Defaulting to Google homepage.'
            url_g = 'https://www.google.com/'

        else:
            url_g = searchObj.group(1)
        # do not append query here; the purpose of -l is to access first link of results

    elif argList.i == True: # Images
        baseURL = 'https://www.google.com'
        req = urllib2.Request(url_g, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"}) 
        con = urllib2.urlopen(req).read()
        searchObj = re.search( r'<a class="q qs" href="([^"]*)">Images</a>', con)

        if not searchObj:
            print 'Warning: no search terms detected. Defaulting to Google Images homepage.'
            url_g = 'https://images.google.com/'

        else:
            imgHash = searchObj.group(1)
            imgHash = imgHash.replace('&amp;', '&')
            url_g = baseURL + imgHash
        # do not append query here; Google Images has a more complex URL, which is handled by the above logic

    elif argList.m == True: # Let Me Google That For You
        url_g = 'http://www.lmgtfy.com/?q='
        url_g += query
        # append query here to pass search terms to LMGTFY

    # additional options here

def main():
    '''
    Driver function for pls
    '''
    DEVNULL = open(os.devnull, 'w')

    initParser()
    validateArgs()
    determineBrowser(parser_g.parse_args())
    determineURL(parser_g.parse_args())

    debugPrint(url_g)

    subprocess.call([browser_g, url_g], stdout=DEVNULL, stderr=subprocess.STDOUT) # shhhh - redirect browser output to /dev/null
    # thanks: http://stackoverflow.com/questions/11269575/how-to-hide-output-of-subprocess-in-python-2-7

if __name__ == '__main__':
    main()
