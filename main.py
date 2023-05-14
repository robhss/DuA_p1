import sys

arg = sys.argv              #list of cmd-line arguments
alg = arg[1]

print(arg[2])
with open(arg[2],'r') as f:
    list = f.readlines

for i in list:
    print[list[i]]

