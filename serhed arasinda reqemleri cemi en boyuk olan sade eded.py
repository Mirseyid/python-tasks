# a ve b araliginda reqemlerinin cemi en boyuk olan sade eded:
while True:
    a = int(input(" birinci serhedi daxil et: "))
    b = int(input(" ikinci serhedi daxil et: "))
    max_cem = 0
    max_eded = 0
    def f(x):# ededin sade ve ya murekkeb oldugunu yoxlayan funksiya
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
        
    def digits(x):# ededin reqemlerinin cemini tapan funksiya
        cem = 0
        while x > 0:
            cem = cem + x % 10
            x = x // 10
        return cem

    for number in range ( a + 1 , b ):
        if f(number) == "sade" and digits(number) >= max_cem and number > max_eded:
            max_cem = digits(number)
            max_eded = number
        else:
            continue
##    print(max_eded)
