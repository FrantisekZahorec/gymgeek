

def vytvor_sachovnici():
    sachovnice = []
    for radek in range(3):
        sachovnice.append([])#přidáme nový řádek s indexem radek od 0 do 2
        for policko in range(3):
            sachovnice[radek].append(" ")#do řádku v přidám políčka s indexem od 2 do 3
    return sachovnice



def zobraz_plochu(plocha):
    for radek in plocha:
        print(radek)


def zadej_vstup(pole, hrac):
    print("Na tahu je hráč {}.".format(hrac))
    vstup = True
    while vstup:
        radek = int(input(" Zadej číslo řádku. ")) - 1
        sloupec = int(input("Zadej číslo sloupce. ")) - 1
        if 0 <= radek < len(pole[0]) and 0 <= sloupec < len(pole):
            if pole[radek][sloupec].upper() not in ["X","O"]:
                vstup = False
                souradnice = [radek, sloupec]
            else:
                print("Políčko je obsazené.")
        else:
            print("Souřadnice mimo rozsah.")
    return souradnice

def zkontroluj(pole, hrac):

    for radek in pole:
        znaku = 0
        for policko in radek:
            if policko == hrac:
                znaku += 1
            else:
                znaku = 0
        if znaku == 3:
            return True
    for y in range(len(pole)): # načítá souřadníci y sloupce
        znaku = 0
        for x in range(len(pole[0])): #načítá souřadnici x řádku
            if pole[x][y] == hrac:
                znaku += 1
            else:
                znaku = 0
        if znaku == 3:
            return True
    #budeme řešit znaky v diagonále zleva a zprava
    zleva = 0
    zprava = 0
    for i in range(len(pole)):
        if pole[i][i] == hrac:
            zleva += 1
        else:
            zleva = 0
        if pole[i][-i-1] == hrac:
            zprava += 1
        else:
            zprava = 0
    if zleva == 3 or zprava == 3:
        return True
    
    return False
    
    
# Hra - 1. a 2. hráč
def hra():
    plocha = vytvor_sachovnici()
    hraci = ["X","O"]
    for tah in range(9):
        zobraz_plochu(plocha)
        hrac = hraci[tah % 2]
        souradnice = zadej_vstup(plocha, hrac)
        plocha[souradnice[0]][souradnice[1]] = hrac
        if zkontroluj(plocha, hrac) == True:
            print("vyhrál hráč {}.".format(hrac))
            return(hrac)
    zobraz_plochu(plocha)
    if zkontroluj(plocha, hrac) == False:
        print("Remíza")

#hra()
"""
hraci_plocha = vytvor_sachovnici()
hraci_plocha [0][2]="X"
hraci_plocha [0][1]=" "
hraci_plocha [2][0]="X"
hraci_plocha [1][1]="X"
zobraz_plochu(hraci_plocha)
a = zkontroluj(hraci_plocha, "X")
print(a)
"""
