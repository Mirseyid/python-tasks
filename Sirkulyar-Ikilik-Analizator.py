# Sirkulyar-Ikilik Analizator
def count_digit(x):
    say = 0
    while x > 0:
        say = say + 1
        x = x // 10
    return say

def rotate_number(x):#ededin birinci reqemini silib ededin sonuna elave edirik
    total = 0
    place = 10
    change_number = x // (10 ** (count_digit(x) - 1))
    x = x % (10 ** (count_digit(x) - 1))
    while x > 0:
        total = total + (x % 10) * place
        place = place * 10
        x = x // 10
    total = total + change_number
    return total


def count_binary_ones(x):# 2 lik say sistemindeki qarsiliginda 1 lerin sayina gore qarsiliq
    total = 0
    count = 0
    while x > 0:
        digit = x % 2
        if digit == 1:
            count = count + 1
            x = x // 2
        else:
            x = x // 2
    if count == 0:
        return 0
    elif count % 2 == 0:
        return 2
    else:
        return 1



def sade_murekkeb(x):# ededin sade ve ya murekkeb oldugunu yoxlayan funksiya
        say = 0
        for bolen in range(2 , x):
            if x % bolen == 0:
                say = +1
            else:
                continue
        if say == 0:
            return "sade"
        else:
           return "murekkeb"

def bolen_cem(x):
    cem = 0
    for bolen in range( 1 , x  ):
        if x % bolen == 0:
            cem = cem + bolen
        else:
            continue
    if cem == x:
        return True
    else:
        return False




def analyze_complex_number(x):
   if sade_murekkeb(x) == "sade" and sade_murekkeb(rotate_number(x)) == "sade":
       return "Category A"
   elif sade_murekkeb(x) != "sade" and count_binary_ones(x) == 2:
       return "Category B"
   elif bolen_cem(x) == True:
       return "Category C"
   else:
       return "Default"

while True:
    number = int(input("Enter the number: "))
    print(f"Original: {number}\nRotated: {rotate_number(number)}\nBinary weight type: {count_binary_ones(number)}\nresult:  {analyze_complex_number(number)}")
