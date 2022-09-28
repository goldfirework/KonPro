Hovedstad = {
    "Norge": "Oslo",
    "Russland": "Moskva",
    "Japan": "Tokyo"
}

Sprak = {
    "Norge": "Norsk",
    "Russland": "Russisk",
    "Japan": "Japansk"
}

Innbyggere = {
    "Norge": "5,455,582",
    "Russland": "146,074,081",
    "Japan": "126,860,301"
}

x = 1
while x < 2:
    svar = input("Hvilket land vil du se fakta om?\n")
    if svar.capitalize() in Hovedstad:
        print("Noen fun facts om " + svar + ":")
        print("Hovedstaden i " + svar.capitalize() + " er: " + Hovedstad[svar.capitalize()])
        print("I " + svar.capitalize() + " snakker de: " + Sprak[svar.capitalize()])
        print("Det bor " + Innbyggere[svar.capitalize()] + " mennesker i " + svar.capitalize())
        x = 3
    else:
        print("Opsie whopsie, "+svar+" er ikke lagret!\nPrøv igjen!\n")
