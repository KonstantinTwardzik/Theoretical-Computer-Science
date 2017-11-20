

####################################################
# kartesisches Produkt
#
from itertools import product

m=5
for t in product((0,1),repeat=m):
    print(t)

# Interpretation als Teilmengen T von I = {0,..,m-1}
# dabei ist i in T gdw. t[i] = 1
I = {0,1,2,3}
for t in product((0,1),repeat=len(I)):
    T ={i for i in I if t[i]}
    print(T)

m=3
k=5
for t in product(range(k),repeat=m):
    print(t)

# Interpretation als endliche totale Funktionen
# f:{0,..,m-1} -> {0,..,k-1} mit f(i)=j gdw. t[i] = j
for t in product(range(k),repeat=m):
    f = { i:t[i] for i in range(m)}
    print(f)


####################################################
# Permutationen
#
from itertools import permutations

m=4
for p in permutations(range(m)):
    print(p)

# Interpretation als Anordnungsmoeglichkeiten
for p in permutations('abc'):
    print(p)
    

####################################################
# Kombinationen: Auswahl von k aus m Elementen 
# ohne Beachtung der Reihenfolge, d.h. {a,b,c}={b,c,a}=...
from itertools import combinations

m=5
k=3
for c in combinations(range(m),k):
    print(c)

# Interpretation als k-elementige Teilmengen T von I = {0,..,m-1}
# dabei ist i in T gdw. i in c
I = {0,1,2,3,4}
k = 3
for c in combinations(range(len(I)),k):
    T = set(c)
    print(T)


