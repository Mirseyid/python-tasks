
import random
first_list = [random.randint(0,10) for i in range(5)]
print(first_list)
second_list = [random.randint(0,10) for i in range(5)]
print(second_list)
ortaq_say = 0
for first in first_list:
    for second in second_list:
        if first == second:
            ortaq_say += 1
        else:
            continue
if ortaq_say > 0:
    print("True")
else:
    print("False")
