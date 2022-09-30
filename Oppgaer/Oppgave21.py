liste = []

n = 0
while n < 5:
    m = 1
    while m < 2:
        try:
            liste.append(int(input("Skriv et tall: ")))
            m = 3
        except:
            print("Wopsie opsie, det funker ikke sjef.")
    n +=1

sum = 0

for x in liste:
    sum += x

for x in liste:
    if x < 10:
        print(str(x), "er mindre enn 10")

if 5 in liste:
    print("5 er i listen!")

print(sum)

print(liste)