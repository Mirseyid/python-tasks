#Istenilen daxil edilmis ededin birinci ve sonuncu reqemlerinin ceminin kvadrat kokunun 3 den boyuk olanlari yoxlayan funksiya
while True:
    def digit(x):#ededin reqemlerinin sayini tapan funksiya
            count = 0
            while x > 0:
                count = count + 1
                x = x // 10
            return count

        
    def ilk_son(x):#ededin ilk ve son reqemlerinin cemini tapan proqram
         cem = 0
         cem = cem + x % 10 + x // (10 ** ( digit(x) - 1 ))
         return cem

    number = int(input("Enter the number: "))
    if ilk_son(number) ** (1 / 2) > 3:
        print("True")
    else:
        print("False")
