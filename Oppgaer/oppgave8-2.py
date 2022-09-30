#Dette er bare den du viste på talva. Se Oppgave2.py for min løsning

print("\n\n\nHei og velkommen til quiz!\n")
poeng = 0

sporsmalsListe = [
    "Hva heter Asias største øy? \n",
    "I hvilket land ligger hovedkontoret til flyselskapet Ryanair? \n",
    "I hvilken by ligger Chryslerbygningen? \n"
    ]
riktigSvar = [
    "borneo",
    "irland",
    "new york"
    ]

x = 0
while x < len(sporsmalsListe):
    svar = input(sporsmalsListe[x])
    if riktigSvar[x] == svar.lower():
        print("\nRiktig!\n")
        poeng += 1
    else:
        print("Feil!")
    x += 1

print("Du fikk " + poeng + " poeng!\n")