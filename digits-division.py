# Print the numbers that are less than or equal to the entered number and are divisible by each of their digits.
while True:
    number = int(input("enter number = "))
    for eded in range(1, number + 1):
        new_number = eded
        ok = True
        while new_number > 0:
            digit = new_number % 10
            if digit == 0 or eded % digit != 0:
                ok = False
                break
            new_number = new_number // 10
        if ok:
            print(eded)
