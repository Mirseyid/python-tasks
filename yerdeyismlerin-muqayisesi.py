def selection_sort(a):
    yerdeyisme = 0
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            yerdeyisme += 1  
        a[i],a[min_index] = a[min_index],a[i]
    return yerdeyisme

def bubble_sort(a):
    N = len(a)
    yerdeyisme = 0
    for i in range(N-1):
        for j in range(N-2,i-1,-1):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                yerdeyisme += 1
    return(yerdeyisme)

import random
a=[random.randint(0,100) for i in range(10)]
b = a[:]
print(a)
print(f"bubble_sortda yerdeyismlerin sayi: {bubble_sort(a)}\nselection_sortda yerdeyismelerin sayi: {selection_sort(b)}") 
