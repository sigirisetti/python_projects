import argparse

# Positional parameters are mandatory

parser = argparse.ArgumentParser()
parser.add_argument("p1", help="first parameter")
parser.add_argument("p2", help="second parameter")
parser.add_argument("p3", help="third parameter", type=int)
args = parser.parse_args()
print(args.p1)
print(args.p2)
print(args.p3)
