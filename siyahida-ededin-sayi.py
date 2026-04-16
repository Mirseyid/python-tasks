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



import random

def bubble_sort(a):
    N =  len(a)
    for i in range(N-1):
        for j in range(N-2,i-1,-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
def binary_search(x,a):
    a = bubble_sort(a)
    count = 0
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        else:
            if x > a[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1
while True:
    my_list =[random.randint(0,11) for i in range(10)]
    print(my_list)
    first_list = my_list[:]
    X = int(input("X ededini daxil edin: "))
    count = 0
    if binary_search(X,my_list) == -1:
        print(f" Massiv: {first_list}\nCesitlenmeden sonra: {bubble_sort(first_list)}\n{X} ededi tapilmadi")
              
    else:    
        while binary_search(X,my_list) != -1:
            count += 1   
            a = my_list[:]
            my_list = []
            for i in range(0,len(a)):  
                if i != binary_search(X,a):
                    my_list += [a[i]]
                else:
                    continue
        print(f"Cesitlenmeden sonra: {bubble_sort(first_list)}\n{X} ededi {count} defe tekrarlanir")
