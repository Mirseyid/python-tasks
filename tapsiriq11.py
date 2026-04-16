def tek_reqem_sayi(x):
    count = 0
    while x > 0:
        s = x % 10
        if s % 2 == 1:
            count += 1
        x = x // 10
    return count
def cut_reqem_sayi(x):
    count = 0
    while x > 0:
        s = x % 10
        if s % 2 == 0:
            count += 1
        x = x // 10
    return count

N = int(input("Listde nece eded olacaq = "))
import random
import copy
my_list = [random.randint(0,100) for i in range(N)]
print(my_list)
N = len(my_list)
a = my_list[:(N//2)]
b = my_list[(N//2):]
for i in range(len(a)-1):
    for j in range((len(a)-2),i-1,-1):
        if tek_reqem_sayi(a[j+1]) < tek_reqem_sayi(a[j]):
            a[j+1],a[j] = a[j],a[j+1]
print(a)

for i in range(len(b)-1):
    for j in range((len(b)-2),i-1,-1):
        if cut_reqem_sayi(b[j+1]) > cut_reqem_sayi(b[j]):
            b[j+1],b[j] = b[j],b[j+1]
print(b)
