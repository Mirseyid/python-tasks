#Dominant sefer ededi

def max_digit(x):#ededin en boyuk reqemini tapiriq
    max_digit = 0
    while x > 0:
        digit = x % 10
        if digit > max_digit:
            max_digit = digit
            x = x // 10
        else:
            x = x // 10
    return max_digit

def count_digit(x):#ededin reqemlerinin sayini tapiriq
    say = 0
    while x > 0:
        say = say + 1
        x = x // 10
    return say
        

def count_binary_ones(x):#2-lik qarsiliginda olan 1 lerin sayi
    total = 0
    count = 0
    while x > 0:
        digit = x % 2
        if digit == 1:
            count = count + 1
            x = x // 2
        else:
            x = x // 2
    return count
while True:
    number = int(input("Enter the number: "))
    
    if count_binary_ones(number) == max_digit(number):
        Result = True
        print(f" Max digit = {max_digit(number)}\n Binary ones count : {count_binary_ones(number)}\n Result: {Result} It is dominant trip  number")
    else:
        Result = False
        print(f" Max digit = {max_digit(number)}\n Binary ones count : {count_binary_ones(number)}\n Result: {Result} It is not dominant trip number")
