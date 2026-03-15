#mukemmel eded

def bolen(x):#ededin bolenlerini tapiriq
    total = " "
    for divide in range( 1 , x ):
        if x % divide == 0 :
            total = total + " " + str(divide)
        else:
            continue
    return total


def bolen_cem(x):#ededin bolenlerinin cemini tapiriq
    cem = 0
    for bolen in range( 1 , x  ):
        if x % bolen == 0:
            cem = cem + bolen
        else:
            continue
    return cem

start = int(input("Araligin 1-ci serhedini daxil edin: "))
end = int(input("Araligin sonuncu serhedini daxil edin: "))

for eded in range( start, end + 1 ):
    if bolen_cem(eded) == eded:
        print(f"Perfect number found:{eded}\nDivisors: {bolen(eded)}")
    else:
        continue
