
####################################################
# Laufzeitmessung mit timeit
#
# gemessen wird die Weltzeit, nicht die CPU-Zeit
# garbage collection ist ausgeschaltet

# Pruefling
from itertools import product
def measure_me(m):
    for t in product((0,1),repeat=m):
        pass


import timeit

# Timer deklarieren
T = timeit.Timer(stmt='measure_me(m)', setup='from __main__ import measure_me, m')

# Testdaten 
m = 22

# Timer aufrufen
#  - repeat: Wiederholungen der Messung, setup je Messung
r = 3
#  - number: Aufrufe des Prueflings (stmt) je Messung 
k = 1
t1 = T.repeat(repeat=r, number=k)  

# Liste der Laufzeiten je Messung in sec (float)
t1      

# Ergebnisse der Messung
print('Bester Wert : ', format(min(t1), '.4f'), 'sec')


