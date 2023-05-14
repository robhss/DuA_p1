unsorted = []


def oeffne(datei: str):
    with open(datei) as file:
        lines = file.readlines()
    unsorted = [line.strip() for line in lines]


def converter(liste: list):
    ergebnis = []
    for x in liste:
        vorname, nachname = x.split()
        ergebnis.append(nachname + " " + vorname)
    return ergebnis


def mergesortwrap(liste: list):
    liste = converter(liste)
    ergebnis = mergesort(liste)
    return converter(ergebnis)


def mergesort(liste: list):
    if len(liste) <= 1:
        return liste
    else:
        index = 0
        lliste = []
        rliste = []

        mid = len(liste)//2

        lliste = liste[:mid]
        rliste = liste[mid:]

        lliste = mergesort(lliste)
        rliste = mergesort(rliste)
        return merge(lliste, rliste)


def merge(lliste: list, rliste: list):
    ergebnis = []
    while len(lliste) != 0 and len(rliste) != 0:
        if lliste[0][1] is not rliste[0][1]:
            if lliste[0][1] <= rliste[0][1]:
                ergebnis.append(lliste[0])
                lliste.pop(0)
            else:
                ergebnis.append(rliste[0])
                rliste.pop(0)
        else:
            if lliste[0][0] <= rliste[0][0]:
                ergebnis.append(lliste[0])
                lliste.pop(0)
            else:
                ergebnis.append(rliste[0])
                rliste.pop(0)
    while len(lliste) != 0:
        ergebnis.append(lliste[0])
        lliste.pop(0)
    while len(rliste) != 0:
        ergebnis.append(rliste[0])
        rliste.pop(0)
    return ergebnis


open("a0020.txt")
result = mergesortwrap(unsorted)
for x in result:
    print(x)
print(unsorted)
