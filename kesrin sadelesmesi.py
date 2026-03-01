'''kesri sadelesdiren funksiya'''
while True:
    suret = int(input("kesrin suretini daxil et: "))
    mexrec = int(input("kesrin mexrecini daxil et: "))
    def modul( x ):
        if x >= 0:
            return x
        else:
            return -x
    def sadelesdirme( a , b ):
        if modul(a) >= modul(b):
            for ortaq_bolen in range( 2 , modul(b) + 1 ):
                if a % ortaq_bolen == 0 and b % ortaq_bolen == 0 :
                    a = a / ortaq_bolen
                    b = b / ortaq_bolen
                else:
                    continue
        else:
            for ortaq_bolen in range( 2 , modul(a) + 1 ):
                if a % ortaq_bolen == 0 and b % ortaq_bolen == 0 :
                    a = a / ortaq_bolen
                    b = b / ortaq_bolen
                else:
                    continue
        return f"{int(a)}/{int(b)}"
    print(sadelesdirme(suret,mexrec))
