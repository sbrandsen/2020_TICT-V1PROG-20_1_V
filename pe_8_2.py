while True:
    woord = input("Voer een woord in van 4 karakters lang: ")
    if len(woord) != 4:
        print(f"{woord} heeft {len(woord)} letters")
    else:
        break

print(f"Inlezen van correcte string: {woord} is geslaagd")