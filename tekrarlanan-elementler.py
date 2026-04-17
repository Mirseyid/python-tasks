def length(list):
    count = 0
    for simvol in list:
        count += 1
    return count
        
import random
tekrarlanan_elementler = ""
tekrarlananlarin_sayi = 0
first_list = []
second_list = []
first_list=[int(input())for i in range(5)]
second_list=[int(input())for i in range(5)]
print(f"list1={first_list}")
print(f"list2 ={second_list}")
for my_index_first in range(length(first_list)):
    for my_index_second in range(length(second_list)):
        if my_index_first == my_index_second and first_list[my_index_first] == second_list[my_index_second]:
            tekrarlanan_elementler += str(first_list[my_index_first]) + " "
            tekrarlananlarin_sayi += 1
        else:
            continue
print(f"Tekrarlanan elementler: {tekrarlanan_elementler}\nEyni indeksde yerleshen elementlerin sayi = {tekrarlananlarin_sayi}")
