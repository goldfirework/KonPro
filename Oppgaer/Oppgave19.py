liste = [6, -4, 7, -2, 8, -3, 9, -11]
minstVerdi = "NULL"
for x in liste:
    if minstVerdi == "NULL":
        minstVerdi = x
    elif x < minstVerdi:
        #print(x, "er mindre enn", minstVerdi)
        minstVerdi = x
    else:
        minstVerdi = minstVerdi
        #print(x, "er ikke mindre enn", minstVerdi)

print(minstVerdi, "er den minste verdien i listen!\n")

størstVerdi = "NULL"

for x in liste:
    if størstVerdi == "NULL":
        størstVerdi = x
    elif x > størstVerdi:
        #print(x, "er større enn", størstVerdi)
        størstVerdi = x
    else:
        størstVerdi = størstVerdi
        #print(x, "er ikke større enn", størstVerdi)

print(størstVerdi, "er den største verdien i listen!")
