
# Typ str: Zeichenketten
w = 'abcd'      # Alternative w = "abcd"
w
v = '12345'
eps = ''        # epsilon = leeres Wort
eps

# Konkatenation
w + v           # wv liefert Fehler
z = 'xy' 'z'    # ok
z = w + '+' + v
w + eps
w + eps == w

# Laenge = Anzahl Symbolpositionen
len(w)
len(w + v) == len(w) + len(v)
len(eps)

# Wiederholung
w*2
w*0
(w + '1')*2
len(w*3)==3*len(w)

# lesender Indexzugriff auf einzelne Symbole
w[0]
w[3]
w[4]    # index out of range

# ABER: Strings sind unveraenderbar! (immutable)
w[0] = 'x' # Fehler


# Slicing: Kopie eines Teilwortes
# liefert stets neue Zeichenkette
w='abcdefg'
w[2:4]  # Teilwort: von Index 2 (inklusiv) bis 4 (exklusiv)
w[:4]   # Praefix: vom Anfang bis Index 4 (exklusiv)
w[4:]   # Suffix: alles ab Index 4 (inklusive)

# Kopie der gesamten Zeichenkette
v = w[:]

# negative Indices zaehlen von rechts
w[-1]   # letztes Zeichen
w[-2]
w[-2:]

# Ersetzen des ersten Zeichens
w = 'x' + w[1:]

'2' in w

# Iteration ueber alle Symbolpositionen
for a in w:
    print(a)

# zugrundeliegendes Alphabet ist immer allumfassend
#     Konzept versch. Alphabete existiert nicht
#     aber endliche Mengen definierbar
Sigma = {'0', '1'}   # ohne direkten Bezug zu anderen Zeichenketten

