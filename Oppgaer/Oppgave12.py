måneder = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
tallListe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tall = False

def foTall():
    n = 1
    while 2 > n:
        tall = input("Hvilken måned vil du ha? 1-12: ")
        try:
            tall = int(tall)
            return(tall)
        except:
            print('"'+ tall + '"' + " er ikke et gyldig valg! Husk at du bare kan skrive tall 1-12!")


m = 1
while 2 > m:
    if tall in tallListe:
        print("Måned nr: " + str(tall) + " er: " + måneder[tall-1].capitalize())
        m = 3
    elif tall == False:
        tall = foTall()
    elif tall != False | isinstance(tall, int):
        print('"' + str(tall) + '"' + " er ikke et gyldig valg! Husk at det bare er 12 måneder!")
        tall = foTall()