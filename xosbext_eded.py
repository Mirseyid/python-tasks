#Faktorial cemi ve xosbextlik analizi


def factorial(x):#faktorial tapma funksiyasi
    power = 1
    total = 1
    while power <= x:
        total = total * power
        power = power + 1
    return total

def get_factorial_sum(x):#ededin reqemlerinin faktoriallarinin cemini tapir
    sum = 0
    while x > 0:
        sum = sum + factorial(x % 10)
        x = x // 10
    return sum
    

def digits_square(x):#reqemlerin kvadratlari cemi
    sum = 0
    while x > 0:
        sum = sum + (x % 10) ** 2
        x = x // 10
    return sum

def is_happy(x):
    while x != 1:
        x = digits_square(x)
        if x == 4:
            return "False"
        else:
            continue
    return "True"


while True:
    number = int(input("Ededi daxil edin: "))
    print(f" Faktorial cem: {get_factorial_sum(number)}\n Xosbextdirmi: {is_happy(number)}")
