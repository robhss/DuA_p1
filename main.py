import sys
from mergeSort import mergesort

arg = sys.argv  # list of cmd-line arguments
alg = arg[1]

# p = r"C:\Users\Robin\Documents\DuA_Pra\DuA_p1\Test-data\a0020.txt"
# with open(p,'r') as f:
#    list = f.readlines()
with open(fr"{arg[2]}", 'r') as f:
    liste = f.readlines()

unsorted = []

for i in liste:
    i = i[:-1]
    unsorted.append(
        [i[:-(len(i) - i.index(" "))], i[i.index(" ") + 1:]])  # erzeugt 2 dimensionale Liste mit vornamen und namen

sortiert = []
if arg[1] == "-mergesort":
    sortiert = mergesort(unsorted)
elif arg[1] == "-quicksort":
    # sorted = quicksort(unsorted)
    pass

s = str
for i in sortiert:
    s = "{p1}{p2} {p3}\n".format(p1=s, p2=i[0], p3=i[1])

print(s)
