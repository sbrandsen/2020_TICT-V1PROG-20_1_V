leeftijd = int(input("Wat is je leeftijd?: "))
heeftNLPaspoortString = input("Heb je een Nederlands paspoort? (ja/nee): ")

heeftNLPaspoort = False

if heeftNLPaspoortString.lower() == "ja":
    heeftNLPaspoort = True

if leeftijd >= 18 and heeftNLPaspoort:
    print("Je mag stemmen!")
else:
    print("Je mag helaas niet stemmen")