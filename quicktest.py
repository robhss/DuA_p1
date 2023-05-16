def quicksort(liste):
    quick(liste,0,len(liste)-1)
    return liste

def quick(liste, links, rechts):
    if links < rechts:
        teiler=teile(liste,links,rechts)
        quick(liste,links,teiler-1)
        quick(liste,teiler+1,rechts)

def teile(liste, links, rechts):
    r=links
    s=rechts-1
    pivot=liste[rechts]
    while r < s:
        while r < s and liste[r]<=pivot:
            r+=1
        while s > r and liste[s] > pivot:
            s=s-1
        if liste[r] > liste[s]:
            temp=liste[r]
            liste[r]=liste[s]
            liste[s]=temp
    if liste[r] > pivot:
        temp = liste[r]
        liste[r] = liste[rechts]
        liste[rechts] = temp
    else:
        r=rechts
    return r
