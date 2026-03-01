#n-ci sade ededi tapan proqram
while True:
    n = int(input("necenci sade ededi isteyirsiniz: "))
    sira = 0
    first_sade = 2
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
    while sira < n:
        if f(first_sade) == "sade":
            sira = sira + 1
            first_sade = first_sade + 1
            
        else:
            first_sade = first_sade + 1
    print(first_sade-1)
