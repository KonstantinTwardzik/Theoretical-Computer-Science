#
# mit cut&paste im Py-Interpreter nachvollziehen!
#

# interaktiver Python-Interpreter
# primary prompt >>>

# Ausdruecke werden unmittelbar ausgewertet
3 + 7
28 * 5
2**5

2**768


# Anweisungen werden sofort ausgefuehrt
x = 123
print(x) 

# Verzweigungen
#     secondary prompt ...
if x >= 0:
    print('war positiv')
    x = -x
else:
    print('ist negativ')


# Blockbildung durch Einruecktiefe (4 x SPACE)
# Abschluss durch Leerzeile


# for-Schleife
#     range()
for i in range(0,10):
    print(i)
    print('----')

# while-Schleife
i = 10
x = 0
while (i > 0):
    i = i - 1
    x = x + 2

# Leerzeilen muessen wirklich leer sein, d.h. auch ohne Space


# Funktionsdeklaration
def f(x):
    if x < 0:
        x = -x
        z = x + 1
    else:
        z = x - 1 
    return z

# Name f ist nun gebunden
#     Typ: function
#     Kontext: __main__ (top-level-Modul)
f 

# Funkionsaufrufe
f(3)
f(0)
f(-2)

# Vergleiche und Wahrheitswerte
f(10) == 11
f(0) == -1

b = True
if b:
    print(not b)

# Python ist case-sensitive
true = True
true
type(true)
true == False
true = False
    


# gerade oder ungerade ? 
def g(y):
    while (y >= 2):
        y = y - 2
    return y

for i in range(20):     # untere Grenze 0
    print(i, g(i))



