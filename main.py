import sys
from mergeSort import mergesort
from compare import compareData
from quicktest import quicksort

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
    unsorted.append([i[:-(len(i) - i.index(" "))], i[i.index(" ") + 1:]])  # erzeugt 2 dimensionale Liste mit vornamen und namen

sorted = []
if arg[1] == "-mergesort":
    sorted = mergesort(unsorted)
elif arg[1] == "-quicksort":
    sorted = quicksort(unsorted)
    pass

s = ''
for i in sorted:
    s = "{p1}{p2} {p3}\n".format(p1=s, p2=i[0], p3=i[1])

#print(sorted)
print(s[:-1])

if sorted == compareData("{p1}.sol".format(p1 = arg[2])):
    print(True)
else:
    print(False)

#print(compareData("{p1}.sol".format(p1 = arg[2])))