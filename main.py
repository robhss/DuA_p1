import sys
from mergeSort import mergesort
from quickSort import quicksort

#sys.setrecursionlimit(10000)

arg = sys.argv  # list of cmd-line arguments
alg = arg[1]


with open(fr"{arg[2]}", 'r') as f:
    liste = f.readlines()

unsorted = []

for i in liste:
    i = i[:-1]
    print(i)
    unsorted.append([i[:-(len(i) - i.index(" "))], i[i.index(" ") + 1:]])  # erzeugt 2 dimensionale Liste mit vornamen und namen

sorted = []
if arg[1] == "-merge":
    sorted = mergesort(unsorted)
elif arg[1] == "-quick":
    sorted = quicksort(unsorted)
    pass

s = ''
for i in sorted:
    s = "{p1}{p2} {p3}\n".format(p1=s, p2=i[0], p3=i[1])

print(s[:-1])