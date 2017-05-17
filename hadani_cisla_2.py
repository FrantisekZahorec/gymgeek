from random import randrange

MAX = 100
number = randrange(MAX) + 1
print("Hádej číslo od 1 do %d. Máš na to 8 pokusů"%(MAX))

def get_guess():
    while True:
        n = input("Hádej ")
        if n.isnumeric():
            n=int(n)
            if 1<= n <= MAX:
                return n
        print("zadadné číslo musí být v intervalu <0; %d>)"%MAX)

remaining_attempts = 8
guess= None

#Hlavní cyklus - jádro hry
while remaining_attempts > 0 and guess != number:
    guess = get_guess()
    if guess < number:
        print("Hledané číslo je větší! :P")
    if guess > number:
        print("Hledanné číslo je menší! Odvážnému štěstí přeje, zkoušej to dál. :)")
    remaining_attempts -= 1

#Vyhodnocení
if number == guess:
    print ("Vyhrál jsi a použil jsi %d pokusů"%(8-remaining_attempts))
else:
    print("Prohrál jsi. Hádané číslo bylo %d."%(number)) 
