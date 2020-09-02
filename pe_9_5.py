uurLoon = ""
urengewerkt = ""

while True:
    try:
        uurLoon = float(input("Wat verdien je per uur: "))
        urenGewerkt = float(input("Hoeveel uur heb je gewerkt: "))
        break
    except:
        print("Please enter a number")

print(f"{round(urenGewerkt)} uur werken levert €{round(uurLoon) * round(urenGewerkt)} op")
