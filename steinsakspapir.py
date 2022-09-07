import random

valg = ["stein", "saks", "papir"]
maskinValg = random.choice(valg)
n = 1
while n < 3:
    try:
        brukerValg = str(input("Velg mellom stein, saks og papir: "))
        if brukerValg.lower() == "stein":
            brukerValg = brukerValg
            n = 4
        elif brukerValg.lower() == "saks":
            brukerValg = brukerValg
            n = 4
        elif brukerValg.lower() == "papir":
            brukerValg = brukerValg
            n = 4
    except:
        print("Venligst bare skriv inn tekst.")
print("Maskinen valgte: " + maskinValg)
if valg.index(brukerValg) == valg.index(maskinValg):
    print("Uavgjort")
elif valg.index(brukerValg) == 2 and valg.index(maskinValg) == 0:
    print("Riktig!")
elif valg.index(maskinValg) == 2 and valg.index(brukerValg) == 0:
    print("Feil!")
elif valg.index(brukerValg) < valg.index(maskinValg):
    print("Riktig!")
elif valg.index(maskinValg) < valg.index(brukerValg):
    print("Feil!")