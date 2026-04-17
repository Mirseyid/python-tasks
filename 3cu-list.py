def length(list):
    count = 0
    for simvol in list:
        count += 1
    return count
N = int(input("Listde nece simvol olacaq: "))
first_list = []
first_list=[input()for i in range(N)]
second_list = []
second_list=[input()for i in range(N)]
print(f"list1={first_list}")
print(f"list2 ={second_list}")
third_list =[]
yeni_list = []
for my_index_first in range(length(first_list)):
    for my_index_second in range(length(second_list)):
         if my_index_first == my_index_second:
             third_list += [first_list[my_index_first] + second_list[my_index_second]]
             yeni_list += [third_list]
             third_list = []
print(f"Yeni list = {yeni_list}")
