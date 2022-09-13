import random

navneListe = ["Jon", "Trygve", "Kar$ten", "Kar$ten"]

nyttNanv = str(input("Hvem har jeg glemt?\n"))
navneListe.append(nyttNanv)

print(navneListe)

navneListe.pop()

print(navneListe)

navneListe.remove("Kar$ten")

print(navneListe)

index = random.randint(0, len(navneListe))
navneListe.pop(index)
print(navneListe)