import random
import copy
my_list = [random.randint(0,1000)for i in range(20)]
print(my_list)
N = len(my_list)
a = my_list[:(N//2)]
b = my_list[(N//2):]
def reqemlerin_cemi(x):
    cem=0
    while x > 0:
        cem = cem + x % 10
        x = x // 10
    return cem


def sifirlarin_sayi(x):
    count = 0
    while x > 0:
        s = x % 10
        if s != 0:
            count += 1
        x = x // 10
    return count
n=len(a)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if sifirlarin_sayi(a[j]) < sifirlarin_sayi(a[min_index]):
            min_index = j
    a[i],a[min_index] = a[min_index],a[i]


t = len(b)
for i in range(t):
    min_index = i
    for j in range(i+1,t):
        if reqemlerin_cemi(b[j]) > reqemlerin_cemi(b[min_index]):
            min_index = j
    b[i],b[min_index] = b[min_index],b[i]
print(a+b)
