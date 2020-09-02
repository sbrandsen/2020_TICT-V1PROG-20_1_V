def namen():
    naamDict = {}
    while True:
        naam = input("Volgende naam: ")
        if naam:
            if naam in naamDict:
                naamDict[naam] += 1
            else:
                naamDict[naam] = 1
        else:
            for key, value in naamDict.items():
                if value == 1:
                    print(f"Er is {value} student met de naam {key}")
                else:
                    print(f"Er zijn {value} studenten met de naam {key}")
            break


namen()
