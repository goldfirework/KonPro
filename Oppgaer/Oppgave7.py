alder = input("Hvor gammel er du: ")

n = 1
while 2 > n:
    try:
        alder = int(alder)
        n = 3
    except:
        alder = input('"' + alder + '"' + " er ikke en alder. Skriv inn alder: ")

n = 1
while 2 > n:
    alderStr = str(alder)
    if alder < 9:
        print("Billetten er gratis for " + alderStr + " åringer!")
    elif alder <= 17:
        print("Billetten koster 20kr for " + alderStr + " åringer!")
    elif alder <= 65:
        print("Billetten koster 40kr for " + alderStr + " åringer!")
    elif alder > 65:
        print("Billetten koster 20kr for " + alderStr + " åringer!")
    n = 3