N = int(input("Musbet tam ededi daxil edin: "))
bolen_list = [x for x in range(1,N+1) if N % x == 0]
print(f" bolenlerin siyahisi = {bolen_list}")
