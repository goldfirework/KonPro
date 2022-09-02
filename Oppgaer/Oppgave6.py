stad = input("Hvilken hovedstad: ")

n = 1
while 2 > n:
    if len(stad) < 1:
        stad = input("Du er nødt til å skrive inn en hovedstad: ")
    else:
        n = 3

hovedstader = ["oslo", "københavn", "stockholm"]
land = ["Norge", "Danmark", "Sverige"]

n = 1
while 2 > n:
    stad = stad.replace(" ", "").lower()
    if stad in hovedstader:
        stadPos = hovedstader.index(stad)
        hovedLand = land[stadPos]
        print(stad.capitalize() + " er hovedstaden i " + hovedLand)
        n = 3
    else:
        stad = input('Fant ikke "' + stad + '"' +", skriv inn igjen: ")