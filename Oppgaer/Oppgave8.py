poengsum = 0
def quest(type, question, answer1, answer2, answer3, answer4, riktig, range, poeng):
    #type 1 = tall spørsmål, kun et svar.
    #type 2 = multi svar spørsmål. 1-4 svar
    #type = velg 1 eller 2 : answer1 bruker av både type 1 og type 2 : answer2-4 brukes bare av type 2 sett til 0 på type 1.
    #riktig brukes bare av type 2, velg riktig svar : range brukes bare av type 1 for å sette godkjent +-
    #poeng setter hvor mye poeng spørsmålet skal gi
    if type == 1:
        print(question)
        answer = input()
        n = 1
        while 2 > n:
            try:
                answer = int(answer)
                n = 3
            except:
                answer = input("Venligst bare skriv inn tall: ")
        if int(str(answer1-answer).replace("-", "")) <= range:
            print("Riktig!")
            return(poeng)
        else:
            print("Feil! Riktig svar var " + str(answer1))
            return(0)
    elif type == 2:
        print(question)
        answers = 0
        if answer1 != 0:
            answers = answers + 1
        if answer2 != 0:
            answers = answers + 1
        if answer3 != 0:
            answers = answers + 1
        if answer4 != 0:
            answers = answers + 1
        if answers == 1:
            return("Bruk type 1, type 2 er for fler-svars oppgaver.")
        elif answers == 2:
            print("[1]"+ str(answer1) + "     [2]"+str(answer2))
        elif answers == 3:
            print("[1]"+ str(answer1) + "     [2]"+str(answer2))
            print("[3]"+ str(answer3))
        elif answers == 4:
            print("[1]"+ str(answer1) + "     [2]"+str(answer2))
            print("[3]"+ str(answer3) + "     [4]"+str(answer4))
        answer = input("Svar: ")
        n = 1
        while 2 > n:
            try:
                answer = int(answer)
                if answer > answers:
                    answer = input("Venligst velg et av svar alternativene, skriv inn 1-" + str(answers) + ": ")
                else:
                    n = 3
            except:
                answer = input("Venligst bare skriv inn tall 1-" + str(answers) + ":")
        n = 1
        if answer == riktig:
            print("Riktig!")
            return(poeng)
        else:
            print("Feil! Riktig svar var nr " + str(riktig))
            return(0)
    else:
        print("bare velg mellom type 1 og 2")

poengsum = poengsum + quest(1, "Hvor høy er verdens høyeste bygning?", 828, 0, 0, 0, 1, 10, 1)
poengsum = poengsum + quest(2, "Hvor raskt løper et rovdyr?", 30, 50, 70, 80, 3, 0, 1)
poengsum = poengsum + quest(2, "Hva er en velosiped", "Ord for fart", "Ord for akselerasjon", "En sykkel", 0, 3, 0, 1)
print("Du fikk " + str(poengsum) + " poeng")