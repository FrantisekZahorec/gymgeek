"""
Šachovnice je 2D pole.
Proto si ji zobrazíme jako seznam obsahující řádky.
Každý řádek obsahuje políčka odpovídající sloupcům.
"""

def vytvor_sachovnici():
    sachovnice = []
    for radek in range(3):
        sachovnice.append([]) #přidáme nový řádek s indexem radek od 0 do 2
        for policko in range(3):
            sachovnice[radek].append(" ") #do řádku v přidám políčka s indexem od 2 do 3
    return sachovnice

#hraci_plocha = vytvor_sachovnici()

def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)
        
#zobraz_plochu(hraci_plocha)

def zkontroluj(plocha, hrac):
    for radek in plocha:
        znaku = 0
        for policko in radek:
            if policko == hrac:
                znaku += 1
            else:
                znaku = 0
        if znaku == 3:
            return True
    for cislo_sloupce in range(3):
        znaku = 0
        for cislo_radku in range(3):
            if plocha[cislo_radku][cislo_sloupce] == hrac:
                znaku += 1
            else:
                znaku = 0
        if znaku == 3:
            return True
    zleva = 0
    zprava = 0
    for i in range(3):
        if plocha[i][i] == hrac:
            zleva += 1
        else:
            zleva = 0
        if plocha[i][2 - i] == hrac:
            zprava += 1
        else:
            zprava = 0
    if zleva == 3 or zprava == 3:
        return True
    return False
    

def zadej_vstup(pole, hrac):
    print("Na tahu je hráč {}.".format(hrac))
    vstup = True
    while vstup:
        radek = int(input("Zadej číslo řádku. ")) - 1
        sloupec = int(input("Zadej číslo sloupce. ")) - 1
        if 0 <= radek < len(pole[0]) and 0 <= sloupec < len(pole):
            if pole[radek][sloupec].upper() not in "X","O":
                vstup = False
                souradnice = [radek, sloupec]
            else:
                print("Políčko je obsazené.")
        else:
            print("Souřadnice mimo rozsah.")
    return souradnice
    
# Hra - 1. a 2. hráč

def hra():
    plocha = vytvor_sachovnici()
    hraci = ["X","O"]
    for tah in range(9):
        zobraz_plochu(plocha)
        hrac = hraci[tah % 2]
        souradnice = zadej_vstup(plocha, hrac)
        plocha[souradnice[0]][souradnice[1]] = hrac
    zobraz_plochu(plocha)

#hra()
testovaci_plocha = vytvor_sachovnici()
testovaci_plocha [0][0] = "X"
testovaci_plocha [1][0] = "X"
testovaci_plocha [2][0] = "X"
zobraz_plochu(testovaci_plocha)
print(zkontroluj(testovaci_plocha, "X"))
