unsorted = ["ba b", "fadfa dedea", "fcdbf cd", "fdded abcab", "dbebc effdc", "abded effdc", "edbfb effdc",
            "cdcdc effdc", "dcaaa daeeb", "adeca daeeb", "deac c", "fa f", "eabbd f", "fcdad ddcce", "ebffd bffbe",
            "fcfea bffbe", "accc eebea", "fa eebea", "adaeb eebea", "bebfd d"]


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
        while index < len(liste):
            if index < len(liste) // 2:
                lliste.append(liste[index])
            if index > len(liste) // 2:
                rliste.append(liste[index])
            index += 1
        lliste = mergesort(lliste)
        rliste = mergesort(rliste)
        return merge(lliste, rliste)


def merge(lliste: list, rliste: list):
    ergebnis = []
    while len(lliste) != 0 and len(rliste) != 0:
        if lliste[0] <= rliste[0]:
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


result = mergesortwrap(unsorted)
for x in result:
    print(x)
