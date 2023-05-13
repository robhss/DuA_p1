import sys

arg = sys.argv              #list of cmd-line arguments
alg = arg[1]

with open(arg[2]) as f:
    list = f.readlines