
# Listen
a = [10, 11, 12, 13] # Liste ganzer Zahlen
len(a)               # Anzahl ELemente


# Index-Zugriff
a[0]
a[3]
a[4]        # index out of bounds  
a[1:3]      # Slicing wie bei str

# Kopieren der Referenz
b = a

# Slicing liefert neue Liste als flache Kopie
c = a[0:2]

# Listen sind aenderbar
a[1] = 110
a.append(14)    # am Ende anfuegen
b[1] == 110     # auch b zeigt auf geaenderte Liste
c[1] == 11      # Kopie c wurde nicht geaendert

# Listen aneinanderhaengen
d = a + b       # neue Liste aus Kopien von a,b
c += a          # Kopie von a anfuegen


# Vorkommen
10 in a

# Elemente loeschen
len(a)
del a[2]
len(a)

# iterieren
for x in c:
    print(x+x)

# Listen vergleichen
a = [1,2,3]
b = [1,2,3]
a==b            # gleiche Werte?
a is b          # identische Objekte?

# unpacking
[x, y, z] = a

