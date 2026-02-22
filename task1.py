# Take a letter from the user and check whether it is a vowel, a consonant, or both 
herf = input("enter herf=")
if herf >= "a" and herf >= "z" or herf >= "A" and herf >= "Z":
    if herf == "a" or "e" or "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U":
        print("Entered alphabet is a constant!")
    elif herf == "y" or "Y": 
        print("Sometimes it is vovel, and sometimes it is a consonant!")
    else:
        print("Entered alphabet is a constant!")
else:
    print("value error")
