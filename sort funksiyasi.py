###sort funksiyasi
a = float(input("Birinci ededi daxil edin: "))
b = float(input("Ikinci ededi daxil edin: "))
c = float(input("Ucuncu ededi daxil edin: "))
def sort(a , b , c ):
    if a >= b and a >= c :
        if b >= c:
            return c , b , a
        else:
            return b , c , a
    elif b >= a and b >= c:
        if a >= c:
            return c , a , b
        else:
            return a , c , b
    else:
        if b >= a:
            return a , b , c
        else:
            return b , a , c
print(sort(a,b,c))
