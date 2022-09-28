#   Del 1:
n = 0
while n < 2:
    try:
        svar = int(input("Hvilket tall skal jeg telle opp til?\n"))
        n = 3
    except:
        print("Du må svare med et tall!")
x = 0

if svar != 0:
    if svar < 0:
        print("Går ikke med negative tall!")
    else:
        while x <= svar:
            print(x)
            x += 1
else:
    print("0")

#   Del 2. Skjønte ikke denne helt

n = 0 
while n < 2:
    print("Hei!")
    svar = input("Skriv slutt for å slutte, og alt annet for å fortsette: ")
    if svar.lower() == "slutt":
        n = 3

#   Del 3. Denne var faktisk umulig å forstå

n=0
while n < 1:
    try:
        repeat = int(input("Hvor mange ganger skal jeg gjenta?\n"))
        n = 2
    except:
        print("Må være et tall!")
x = 0        
while x < repeat:
    print("Hei!")
    x += 1