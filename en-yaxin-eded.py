while True:
    import random
    a = [random.randint(0,20) for i in range (10)]
    print(f"Massiv: {a}")
    def maks_eded(t):
        maks = float("-inf")
        for i in t:
            if i > maks:
                maks = i
        return maks
    def minimal_eded(t):
        minimal = float("inf")
        for i in t:
            if i < minimal:
                minimal = i
        return minimal

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
                return a[mid]
            else:
                if x > a[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
    print(f"Cesidlemeden sonra: {bubble_sort(a)}")
    X = int(input("X ededi daxil edin: "))
    if binary_search(X,a) == -1:
        if X >= maks_eded(a):#daxil edilen ededin siyahinin maksimal ededinden boyuk oldugu hal
            T = X
            while binary_search(T,a) == -1:
                T = T - 1
            print(f"{X} ededi tapilmadi.En yaxin eded: {T}")
        elif X <= minimal_eded(a):#daxil edilen ededin siyahinin minimal ededinden kicik oldugu hal
            J = X
            while binary_search(J,a) == -1:
                J = J + 1
            print(f"{X} ededi tapilmadi.En yaxin eded: {J}")
        else:   
            Y = X#Y deyiseni siyahida daxil edilen edede en yaxin ve ondan kiçik olan ededi tapmaq ucun
            Z = X#Z deyiseni siyahida daxil edilen edede en yaxin ve ondan boyuk olan ededi tapmaq ucun
            while binary_search(Z,a) == -1:
                Z = Z + 1
            while binary_search(Y,a) == -1:
                Y = Y - 1
            if (Z - X) < (X - Y):
                print(f"{X} ededi tapilmadi.En yaxin eded: {Z}")
            elif (Z - X) > (X - Y):
                print(f"{X} ededi tapilmadi.En yaxin eded: {Y}")
            else:
                print(f"{X} ededi tapilmadi.En yaxin eded: {Y} ve {Z}")
    else:
         print(f"{X} ededi tapildi")
