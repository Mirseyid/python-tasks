def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    
    left=[x for x in a[1:] if x <= pivot]
    right=[x for x in a[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

N = int(input("Nece setir daxil edilecek: "))
A =[input()[2:] for i in range(N)]
print(f"Sozlerin elifba sirasina gore duzulusu:{quick_sort(A)}")
