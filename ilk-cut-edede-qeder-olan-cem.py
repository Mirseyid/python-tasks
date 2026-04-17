while True:
    N = int(input("Listde nece eded olacaq = "))
    import random
    my_list = [random.randint(0,10) for i in range(N)]
    tek_ededlerin_cemi = 0
    for eded in my_list:
        if eded % 2 == 1:
            tek_ededlerin_cemi += eded
        else:
            break
    print(f"list = {my_list}\nListin ilk cut ededine qeder olan cem: {tek_ededlerin_cemi}")
