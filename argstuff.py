import argparse
parser = argparse.ArgumentParser()

parser.add_argument('terms', nargs='*')
parser.add_argument('-c')
parser.add_argument('-f')
parser.add_argument('-l')
parser.add_argument('-s')
parser.add_argument('-i')
parser.add_argument('-m', '--sass')
parser.add_argument('-d')
# parser.add_argument('-h', '--help')


args = parser.parse_args()
print args.terms
