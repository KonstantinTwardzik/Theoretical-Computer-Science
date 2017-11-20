
# Assoziative Listen
d = {}      # leeres Dictionary
d['a'] = 1  # key-value-Paare einfuegen
d['b'] = 2
d['c'] = 3

d['b']      # Zugriff ueber key
d['b'] = 5  # Ueberschreiben

len(d)      # Anzahl key-value-Paare


# ideal zur Repraesentation endlicher Funktionen
f = {}
f[-2] = 2
f[-1] = 3
f[0] = 'n.d.'
f[1] = 0

# alternative Konstruktion
g={'A': ['Auto', 'Asteroid'], 'B': ['Ball','Berg', 'Burg']}
g['A'][0]


# Vorkommen via key
'c' in d

# key-value-Paar loeschen
len(d)
del d['b']
len(d)

d['b']      # Fehler

# iterieren
for key in d:
    print(key, d[key])

for key,val in d.items():
    print(key,val)

for key in d.keys():
    print(key)

for val in d.values():
    print(val)




