
###########################################################
# Graphen

# Repraesentation von G als Liste von Adjazenzmengen, die
# pro Knoten dessen Nachbarn enthalten:
#
# fuer alle v aus V ist G[v] = { w | {v,w} in E } 
#


# Beispiel: Sei G=(V,E) mit
# m = 6 Knoten in V = {0,1,2,3,4,5} und
# k = 7 Kanten in E = { {0,1},{0,2},{1,2},{1,5},{2,3},{2,5},{3,5} }

# jede Kante kommt doppelt vor

def define_G1():
    m = 6
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2,5}
    G[2] |= {0,1,3,5}
    G[3] |= {2,5}
    # G[4] ist leer
    G[5] |= {1,2,3}
    return G


# Verwendung
G = define_G1()

# Anzahl Knoten
m = len(G)

# Anzahl Kanten in ungerichtetem Graph in O(m)
k = sum(len(G[i]) for i in range(m)) // 2 

# Test auf Nachbarschaft
2 in G[3]   
1 in G[4]   

# Grad eines Knotens
d = len(G[2])

# alle Nachbarn
for w in G[2]:
    print(w)
