import argparse

def trueCount(pants):
	count = 0 # number of true items in the list
	for current in pants:
		if current is True:
			count += 1
	return count

parser = argparse.ArgumentParser()

parser.add_argument(
		'terms',
		nargs='*')
parser.add_argument(
		'-c',
		help='open using Chrome',
		action='store_true')
parser.add_argument(
		'-f',
		help='open using Firefox',
		action='store_true')
parser.add_argument(
		'-l',
		help='I\'m Feeling Lucky',
		action='store_true')
parser.add_argument(
		'-s',
		help='search using Google Scholar',
		action='store_true')
parser.add_argument(
		'-i',
		help='search using Google Images',
		action='store_true')
parser.add_argument(
		'-m',
		help='increase sass - search using Let Me Google That For You',
		action='store_true')
parser.add_argument(
		'-d',
		help='debug flag - prints the URL that pls will open',
		action='store_true')
# parser.add_argument('-h', '--help')

args = parser.parse_args()

# Group conflicting options
browserArgs = []
browserArgs.append(args.c)
browserArgs.append(args.f)

flagArgs = []
flagArgs.append(args.l)
flagArgs.append(args.s)
flagArgs.append(args.i)
flagArgs.append(args.m)

browserTrueCount = trueCount(browserArgs)
flagTrueCount = trueCount(flagArgs)
print 'browser: ' + str(browserTrueCount)
print 'flag: ' + str(flagTrueCount)

if browserTrueCount > 1:
	# give error message that only one browser can be specified
	# or use system default

if flagTrueCount > 1:
	# give error message that only one flag of the set [s,l,i,m] can be used at once

# conflicting groups:

# If one argument in a given set is chosen, no others from that set may be chosen.

# [c,f] [s,l,i,m]
