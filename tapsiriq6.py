import random
N = int(input("Siyahida nece eded olacaq: "))
my_list=[random.randint(-100,100) for i in range(N)]
netice = quick_sort(my_list)
musbet = 0
for i in netice:
    if i > 0:
        musbet += 1
    else:
        continue
print(f"Massiv:{my_list}\nNetice:{netice}\nMusbet elementlerin sayi: {musbet}")
