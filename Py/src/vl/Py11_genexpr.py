
#
# besondere Ausdruecke:
#    generator expressions mit lazy evaluation
#    runde Klammern!

# liefert iterierbares Objekt
(i*i for i in range(10))

gen = (i*i for i in range(10))

next(gen)
next(gen)
next(gen)
next(gen)


# gedacht fuer Funktionen, die iterierbare Objekte (iterables) erwarten
# ohne dass das Zwischenergebnis relevant ist
# z.B. sum(), min(), max()
sum(i*i for i in range(10))

# muesste eigentlich so aussehen, aber Kurzform erlaubt:
sum((i*i for i in range(10)))


sum(i*i for i in range(10) if i%2)

# ist aequivalent zu:
b = 0
for i in range(10):
    if i%2:
        b += i*i

print(b)


s = (3,2,5,2,8,5,2,4,3)             # tuple
m = len(s)

max1 = max(s[i] for i in range(m))  # O(m)
max2 = max(a for a in s)
max1 == max2


# erste Komponente k eines Paares (k,v) mit minimalem v
R = {(1,17),(2,5),(3,12),(4,9)}
(_,k) = min( (v,i) for i,v in R )   # O(len(R))
print(k)

