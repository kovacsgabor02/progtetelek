def elso():
    VEGE = 0
    db = 0
    minimum = 2147483648
    szam = int(input("szam"))
    while szam != VEGE:
        szam = int(input("szam"))
        if szam < minimum:
            minimum = szam
        db += 1

    print(db)
