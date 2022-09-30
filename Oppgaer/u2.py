personer = {}

personer["Jon"] = "90251921"

print(personer)

n = 0
while 2 > n:
    svar = input("Ønsker du legge til en bruker? [y] for ya, alt annet for nei\n").lower
    if svar == "y":
        m = 0
        while m < 1:
            try:
                nanv = str(input("Navnet til personen som skal legges til:\n"))
                m = 2
            except:
                print("Shits pomfrits, må være et navn!")
        m = 0
        while m < 1:
            try: 
                fødselsdato = int(input("Fødselsdatoen til", nanv, ":\n").replace(".", ""))
                m = 2
            except:
                print("Venligst bare skriv inn fødselsdatoen i tall")
    else:
        print("ok")
        n = 3