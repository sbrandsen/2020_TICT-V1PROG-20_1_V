getal = ""
getalCount = 0
getalSum = 0

while getal != 0:
    getal = int(input("Geef een getal: "))
    getalSum += getal
    getalCount += 1

print(f"Er zijn {getalCount} getallen ingevoerd, de som is: {getalSum}")
