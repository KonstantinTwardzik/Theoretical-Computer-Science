
#
# set comprehension: kompakte Konstruktion endlicher Mengen
#

M = {i for i in range(20) if not i%3}
M

# Funktionsanwendung auf die Elemente moeglich
N = {x*x for x in M}
N


# mehrfache Schleifen und Bedingungen
K = {(i,j) for i in [1,2,3] for j in [1,2,3] if i!=j}
K

# ist aequivalent zu:
L = set()
for i in [1,2,3]:
    for j in [3,2,1]:
        if i!=j:
            L |= {(i,j)}

K == L

# Potenzmenge P der Menge S
def powerset(S):                    
    P = {frozenset()}               # frozenset statt set als Mengenelemente
    for e in S:
        P |= {R | {e} for R in P}   # ergaenze jedes R aus P um e
    return P

T = powerset({0,1,2,3})
T
len(T)


################################################################
# gleicher Mechanismus existiert auch fuer list, dict und tuple
#

# list comprehension
a = [2**i for i in range(100)]
a

# dict comprehension (Values werden ueberschrieben)
d = {a:i for a in 'xyz' for i in range(3)}
d

# tuple comprehension
t = tuple( i for i in range(3) )
t


# Unterschied zu gen expr: 
# hier wird die Liste vor der Summenbildung vollstaendig erstellt:
sum([2**i for i in range(100)])
2**100-1 


