import math
N = list(map(int,input("Ededleri bosluqla yaz: ").split()))
my_list = [round(sum((4 * math.sin(i) + 2 * i)/(math.log(9*i,3) * 2**i) for x in N for i in range(1,x+1)),2)]
print(f"N={N}\nList={my_list}")
