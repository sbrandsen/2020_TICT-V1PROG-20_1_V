class Cijfers:
    cijferPROG = 8.7
    cijferPROJA = 7.2
    cijferMOD = 6.5


eu = 30

gemiddelde = round(((Cijfers.cijferPROG + Cijfers.cijferPROJA + Cijfers.cijferMOD) / 3), 1)
print(f"Gemiddelde is {gemiddelde}\n")

totaalBeloning = 0
beloningTemp = 0
vak = ""

for attr, value in vars(Cijfers).items():
    if attr[0:6] == "cijfer":
        beloningTemp = round(eu * value)
        if attr == "cijferPROG":
            vak = "programmeren"
        if attr == "cijferPROJA":
            vak = "project 1"
        if attr == "cijferMOD":
            vak = "modelleren"

        totaalBeloning += beloningTemp
        print(f"Voor {vak} krijg ik een €{beloningTemp} beloning")

print(" \n" + f"Totale beloning is €{totaalBeloning}")

