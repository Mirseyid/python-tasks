#Ededi tersine yazan funksiya
while True:
    number = int(input("Enter the number: "))


    def digit(x):#ededin reqemlerinin sayini tapan funksiya
        count = 0
        while x > 0:
            count = count + 1
            x = x // 10
        return count

    def reverse(x):#ededi tersine ceviren funksiya
        cem = 0
        while x > 0:
            cem = cem + (x % 10) * (10 ** (digit(x) - 1))
            x = x // 10
        return cem
    print(reverse(number))
