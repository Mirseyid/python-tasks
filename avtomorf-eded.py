# Finds all automorphic numbers less than or equal to the entered number
while True:
    say = 0
    cem = 0
    new_say = 0
    number = int(input("enter number = "))
    for eded in range(1,number+1):
        say = 0
        new_number = eded
        # ededin reqemlerinin sayını tapır
        while new_number > 0:
            say = say + 1
            new_number = new_number // 10 
        square = eded ** 2
        # ededin kvadratının son reqemini tapırıq
        if eded == square % ( 10 ** say):
            print(eded)
        else:
            continue
