voornaam = "Stephan"
tussenvoegsel = ''
achternaam = "Brandsen"

# Use "f" before a string to easily format strings with variables
mijnnaam = f"{voornaam} {tussenvoegsel} {achternaam}"

# To remove excess spaces, split to strings, then join them together with a space
mijnnaam = " ".join(mijnnaam.split())

print(mijnnaam)

a = 6
b = 7

c = (a + b) / 2

print(a < 6.75 < b)

# Check if sum of words is equal to mijnnaam, will result in false because of spaces
print(len(mijnnaam) == len(voornaam) + len(tussenvoegsel) + len(achternaam))

# Check if length mijnnaam is at least 5 times bigger than variable c
print(len(mijnnaam) > (c*5))

# Check if tussenvoegsel is not empty, if it isn't then check if it exists in mijnnaam
if tussenvoegsel:
    print(tussenvoegsel in mijnnaam)
else:
    print("No tussenvoegsel entered")





