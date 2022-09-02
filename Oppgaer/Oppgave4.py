a, b = 4, 5

sumAB = a + b
print("Summen av a og b: " + str(sumAB))

CD = input("Skriv inn to tall du vil summere: ").split(" ")
if len(CD) == 2:
    sumABCD = int(CD[0])+int(CD[1])
    print("Summen av c og d: " + str(sumABCD))
else:
    print("Du er nøtt til å skrive to tall med mellom rom mellom!")
