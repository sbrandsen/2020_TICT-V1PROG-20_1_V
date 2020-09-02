import datetime


def hardloperformat():
    hardlopers = []
    while True:
        naamHardloper = input("Wat is de naam van de hardloper?: ")
        vandaag = datetime.datetime.today()
        formattedVandaag = vandaag.strftime("%a %d %b %Y")
        formattedTijd = vandaag.strftime("%X")

        volledigeString = f"{formattedVandaag}, {formattedTijd}, {naamHardloper}"
        hardlopers.append(volledigeString)

        antwoordString = input("Wil je nog een hardloper toevoegen? (ja/nee): ")
        if (antwoordString.lower()) != "ja":
            schrijfnaarbestand(hardlopers)
            break


def schrijfnaarbestand(hardlopers):
    with open("pe_6_4_hardlopers.txt", "a") as f:
        for hardloper in hardlopers:
            f.write("\n" + hardloper)
            print(f"\"{hardloper}\" naar bestand geschreven!")


hardloperformat()
