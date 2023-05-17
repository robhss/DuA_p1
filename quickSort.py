def quicksort(l :list):
    quicksortHelper(l, 0, len(l) - 1)
    return l

def quicksortHelper(l : list, left: int, right: int):
    if left < right:

        p = sort(l, left, right)
        quicksortHelper(l, left, p - 1)
        quicksortHelper(l, p + 1, right)

def sort(l : list, left : int, right : int):

    pivot = l[right]

    i = left - 1

    for j in range(left, right):
        if l[j][1] != pivot[1]:
            if l[j][1] < pivot[1]:

                i += 1
                
                (l[i], l[j]) = (l[j], l[i])
        else:
            if l[j][0] < pivot[0]:

                i += 1
                
                (l[i], l[j]) = (l[j], l[i])

    (l[i + 1], l[right]) = (l[right], l[i + 1])
    
        
    return i + 1