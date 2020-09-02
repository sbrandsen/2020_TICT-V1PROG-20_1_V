with open("pe_6_2_kaartnummers.txt") as f:
    lines = []

    regelCount = 0
    hoogsteKaartnummer = 0
    regelHoogsteKaartnummer = 0

    for line in f:
        regelCount += 1
        kaartnummer = int(line.split(",")[0])
        if kaartnummer > hoogsteKaartnummer:
            hoogsteKaartnummer = kaartnummer
            regelHoogsteKaartnummer = regelCount

    print(f"Deze file telt {regelCount} regels")
    print(f"Het grootste kaartnummer is: {hoogsteKaartnummer} en dat staat op regel {regelHoogsteKaartnummer}")
