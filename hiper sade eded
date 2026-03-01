###hiper sade funksiyasi
while True:
    eded = int(input("Ededi daxil edin: "))
    def sade(x):
        bolen_sayi = 0
        for bolen in range ( 2 , int(x) ):
            if int(x) % bolen == 0:
                bolen_sayi = bolen_sayi + 1
            else:
                continue
        if bolen_sayi == 0:
            return True
        else:
            return False
            
    def hiper_sade(x):
        Ok = True
        while int(x) > 0:
            if sade(int(x)) != True :
                Ok = False
                x = int(x) // 10
            else:
                x = int(x) // 10
        if Ok == True :
            return "Daxil etdiyiniz eded hiper sadedir"
        else:
            return "Daxil etdiyiniz eded hiper sade deyil"
    print(hiper_sade(eded)
