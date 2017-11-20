
# Objekte vom Typ set sind 
# endliche (!) Sammlungen ohne Ordnung und Duplikate
A = {1, 2, 3 ,4}
B = {2, 3, 2, 5}
L = {'011','101', 100}
Sigma = {'0', '1'} 

E = set()      # leere Menge
# F = {} legt dagegen ein leeres Dictionary an


# Test auf Zugehoerigkeit
2 in A   
'3' not in Sigma
1 in E

# Anzahl Elemente
len(B)
len(E)

# Mengen sind iterierbar
for x in A:
    print(x)

# Mengenoperationen
C = A | B       # Vereinigung
D = A.union(B)  # Alternative
C == D

C = A & B       # Durchschnitt
D = A.intersection(B)
C == D

C = A - B       # Differenz
D = A.difference(B)
C == D

# Vergleiche
B <= A          # Teilmenge, auch >=
B.issubset(A)   
{1, 2} < A      # echte Teilmenge, auch >
Sigma.isdisjoint(A)

# Mengen vom Typ set sind aenderbar
# Update-Operationen z.B.
A |= B      # A := A | B
A.add(10)   
A.remove(2) 
# auch discard, clear

# Elemente in Mengen MUESSEN hashable sein:
#    ueber den Wert(!) des Elements wird eine Speicherstelle ermittelt
#    folglich sind aenderbare Typen nicht hashable
# insbesondere Mengen selbst sind NICHT hashable weil aenderbar
# d.h. Mengen von Mengen so nicht definierbar
# P = {{1,2},{2,3}} liefert Typfehler

# Typ frozenset ist immutable (unveraenderbar) und hashable
P = {frozenset({1,2}),frozenset({2,3})}

# alles wie bei set
F = frozenset({1,2})
1 in F
# ausser: update nicht moeglich
F.add(3)


