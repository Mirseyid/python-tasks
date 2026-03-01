#sade vuruqlarin quvvetlerinden en boyuyunu tapan proqram
while True:
    number =int(input("enter the number (it must be >1): "))
    max_quvvet = 0
    vuruq_sayi = 0
    sade_vuruq = 2
    while sade_vuruq <= number :
        while number % sade_vuruq == 0 :
            vuruq_sayi = vuruq_sayi + 1
            number = number // sade_vuruq
        if vuruq_sayi > max_quvvet :
            max_quvvet = vuruq_sayi
        sade_vuruq = sade_vuruq + 1
        vuruq_sayi = 0
    print(max_quvvet)
