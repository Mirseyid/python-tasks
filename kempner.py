#Kempner funksiyasi
while True:
    def fact(x):
        i = 1
        hasil = 1
        while i <= x:
            hasil = hasil * i
            i = i + 1
        return hasil


    def kempner(x):
        eded = 1
        while fact(eded) % x != 0:
            eded = eded + 1
        return eded

    number = int(input("Enter the number: "))
    print (f"{kempner(number)}!")
        
