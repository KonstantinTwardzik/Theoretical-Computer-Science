

# Typ tuple 
t = 1, 'zwei', 3    # ohne Klammern, oder
s = ('A','B')       # aeq. mit runden Klammern     
t                   # Ausgabe immer mit Klammern
len(t)              # Anzahl ELemente


# Index-Zugriff, nur lesend
t[0]
t[3]        # index out of range  
t[-1:]      # Slicing wie bei list und str

# Besonderheit 1-elementige Tupel
one = 'single',     # Komma muss folgen, denn
w = ('single')      # das ist ein String
len(one)
len(w)

empty = ()          # leeres Tupel
len(empty)

# Tupel sind NICHT aenderbar
t[1] = 2        # TypeError
del t[0]        # TypeError

t += s          # aneinanderhaengen
'A' in t        # Vorkommen
for e in t:     # iterieren
    print(e)

# unpacking
v, w = s 