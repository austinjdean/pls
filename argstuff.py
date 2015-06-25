import argparse

parser_g = argparse.ArgumentParser()

def trueCount(pants):
	count = 0 # number of true items in the list
	for current in pants:
		if current is True:
			count += 1
	return count

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
		'-l',
		help='I\'m Feeling Lucky',
		action='store_true')
parser_g.add_argument(
		'-s',
		help='search using Google Scholar',
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
# parser_g.add_argument('-h', '--help')

def getQuery():
	global parser_g
	query = ''
	terms = parser_g.parse_args().terms
	for term in terms:
		query += term
		query += '+'
	query = query[:-1] # remove final '+' added by for loop
	return query

def validateArgs():
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
	# print 'browser: ' + str(browserTrueCount)
	# print 'flag: ' + str(flagTrueCount)

	# print args

	if flagTrueCount > 1:
		# give error message that only one flag of the set [s,l,i,m] can be used at once
		print 'Only one flag from the option set [-s,-l,-i,-m] may be used at once.'
		exit(1)

	if browserTrueCount > 1:
		# give warning message that only one browser can be specified and use system default
		print 'Warning: multiple browsers specified. Using system default browser...'
		browser = 'xdg-open'

print getQuery()
