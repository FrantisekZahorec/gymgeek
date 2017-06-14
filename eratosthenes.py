# Eratosthenovo síto
N = 500
sito = []

for i in range(N):
    sito.append(True)

#print(sito)

def tiskni(sito, sirka=10):
    w = len(str(len(sito)+1))
    for x in range(0, len(sito), sirka):
        for y in range(sirka):
            if x+y < len(sito):
                if sito[x+y]:
                    print(("{:>" + str(w) + "}").format(x+y+1),end=" ")
                else:
                    print(("{:>%s}"%w).format(" "), end=" ")
            else: break
        print()

def find_primes(sito):
    sito[0] = False
    for i in range(1,len(sito)):
        if sito[i]:
            for n in range((i+1)*2-1, len(sito), i+1):
                sito[n]=False
    return(sito)
        
tiskni(find_primes(sito))
