

# prodZ muss deklariert sein
from vl.lek04.prodZ import prodZ

# Idee: teste fuer in Frage kommende n
#       ob x=n*n
def M1(x):
    d = 0
    for n in range(0,(x+1)):
        z = prodZ(n,n)
        if (z == x):
            d = 1
    return d


for x in range(101):
    print(x, M1(x))
