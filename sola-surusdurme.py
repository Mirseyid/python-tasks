N = int(input("Listde nece eded olacaq: "))
first_list = []
first_list=[int(input())for i in range(N)]
print(f"list1={first_list}")




second_list =[first_list[x] for x in range(1,N)]
second_list += [first_list[0]]
print(f"list2 ={second_list}")
