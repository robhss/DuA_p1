import sys

arg = sys.argv              #list of cmd-line arguments
alg = arg[1]

#p = r"C:\Users\Robin\Documents\DuA_Pra\DuA_p1\Test-data\a0020.txt"
with open(fr"{arg[2]}",'r') as f:
    list = f.readlines()

for i in list:
    i = i[:-1]
    print(i)

