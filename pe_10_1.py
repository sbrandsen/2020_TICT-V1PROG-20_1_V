import json
from tabulate import tabulate

# Used tabulate to beautify the output, this is optional

print("Dit zijn de namen, codes en types van elk station:\n")

tableContent = []
hoogsteLong = 0
naamHoogsteLong = ""

with open("10_1JSON.json") as json_file:  # Be sure to have 10_1JSON.json in script directory
    data = json.load(json_file)
    for p in data["payload"]:
        code = p["code"]
        typeStation = p["stationType"]
        naam = p["namen"]["lang"]

        if p["lng"] > hoogsteLong:
            hoogsteLong = p["lng"]
            naamHoogsteLong = naam

        tableContent.append([naam, code, typeStation])

print(tabulate(tableContent) + "\n")
print(f"Het meest oosterlijk gelegen station is: {naamHoogsteLong}")
