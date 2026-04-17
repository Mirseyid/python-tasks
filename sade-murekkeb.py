import random
def sade_or_murekkeb(x):
    bolen_sayi = 0
    for i in range(2,x):
        if x % i == 0:
            bolen_sayi += 1
        else:
            continue
    if bolen_sayi != 0:
        return False
    else:
        return True

N = int(input("Listde nece eded olacaq: "))
A = [random.randint(0,101) for i in range(N)]
B = [x for x in A if sade_or_murekkeb(x) == True]
print(f"A = {A}\nB = {B}")
