#Zencirvari Harshad


def sum_digits(x):#ededin reqemlerinin cemini tapiriq
    sum = 0
    while x > 0:
        sum = sum + x % 10
        x = x // 10
    return sum



def harshad_chain(x):#harshad emeliyyati nece defe ardicil davam edir onu tapiriq
    total_chain = 0
    while x != 1 and int(x / sum_digits(x)) == x / sum_digits(x):
        x = x / sum_digits(x)
        total_chain = total_chain + 1
    return total_chain




while True:
    eded = int(input("Ededi daxil edin: "))
    next_eded = eded
    step = 1

    while eded != 1 and int(eded / sum_digits(eded)) == eded / sum_digits(eded):
        print(f" step{step}: {eded} / {sum_digits(eded)} = {eded/sum_digits(eded)}")
        eded = eded / sum_digits(eded)
        step = step + 1
    print(f" Total chain length: {harshad_chain(next_eded)}")
