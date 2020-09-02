import json

filename = "pe_10_2_inloggers.json"

while True:
    naam = input("Wat is je achternaam?: ")
    voorl = input("Wat zijn je voorletters?: ")
    gbdatum = input("Wat is je geboortedatum?: ")
    email = input("Wat is je e-mail adres?: ")

    accountDict = {"naam": naam,
                   "voorletter": voorl,
                   "gbdatum": gbdatum,
                   "email": email}

    with open(filename, 'w') as f:
        json.dump(accountDict, f)

    if input("Do you want to add another account (y/n): ") == "n":
        print("Exiting...")
        exit()
