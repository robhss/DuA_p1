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
        if lliste[0][1] != rliste[0][1]:
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
