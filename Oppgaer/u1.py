def revListe(liste):
    listeRev = []
    n = 1
    for x in liste:
        siste = len(liste) - n
        sisteStr = liste[siste]
        listeRev.append(sisteStr)
        n += 1
    return(listeRev)

print(revListe(["en", "pluss", "to", "pluss", "tre", "er", "seks"]))