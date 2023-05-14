import sys

arg = sys.argv              #list of cmd-line arguments
alg = arg[1]

#p = r"C:\Users\Robin\Documents\DuA_Pra\DuA_p1\Test-data\a0020.txt"
#with open(p,'r') as f:
#    list = f.readlines()
with open(fr"{arg[2]}",'r') as f:
    list = f.readlines()

unsorted = []

for i in list:
    i = i[:-1]                            
    unsorted.append([i[:-(len(i) - i.index(" "))], i[i.index(" ") + 1:]])                                   #erzeugt 2 dimensionale Liste mit vornamen und namen
    
print(unsorted)


