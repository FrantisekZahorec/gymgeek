from random import randrange

number = randrange(100) + 1
print("Hádej číslo máš 8 pokusů")
MAX = 100
number = randrange(MAX) + 1
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
    remaining_attempts -= 1
if remaining_attempts == guess:
    print ("Vyhrál jsi a použil jsi %d pokusů"%(8-remaining_attempts))
else:
    print("Prohrál jsi. Hádané číslo bylo %d."%(number)) 
