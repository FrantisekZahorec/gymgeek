"""
Šachovnice je 2D pole.
Proto si ji tobrazíme seznam obshující řádky.
Každý řádek obsahuje políčka odpovídající sloupcům.
"""
def vytvor_sachovnici():
    sachovnice = []
    for radek in range(3):
        sachovnice.append([])#přidáme nový řádek s indexem radek od 0 do 2
        for policko in range(3):
            sachovnice[radek].append(" ")#do řádku v přidám políčka s indexem od 2 do 3
    return sachovnice

#hraci_plocha = vytvor_sachovnici()

def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)
#zobraz_plochu(hraci_plocha)

# Hra - 1. a 2. hráč
def hra():
    plocha = vytvor_sachovnici()
    hrac1 = True
    for i in range(9):
        zobraz_plochu(plocha)
        if hrac1 == True:
            print("Hraje 1. hráč.")
            radek = int(input("Zadej číslo řádku."))
            policko = int(input("Zadej číslo sloupce."))
            plocha[radek-1][policko-1] = "X"
            hrac1 = False
        else:
            print("Hraje 2. hráč.")
            radek = int(input("Zadej číslo řádku."))
            policko = int(input("Zadej číslo sloupce."))
            plocha[radek-1][policko-1] = "O"
            hrac1 = True
    zobraz_plochu(plocha)

hra()
