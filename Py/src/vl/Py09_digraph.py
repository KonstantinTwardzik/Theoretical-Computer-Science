
###########################################################
# Digraphen (gerichtete Graphen)

# Beispiel: Sei G=(V,E) mit
# m = 3 Knoten in V = {0,1,2} und
# k = 4 Kanten in E = { (0,1),(1,0),(0,2),(1,2)}

# jede Kante kommt einmal vor

def define_G2():
    m = 3
    G = [set() for _ in range(m)]   # alle Mengen leer anlegen
    G[0] |= {1,2}
    G[1] |= {0,2}
    # G[2] ist leer
    return G

# Verwendung
G = define_G2()

# Anzahl Knoten
m = len(G)

# Anzahl Kanten in Digraph in O(m)
k = sum(len(G[i]) for i in range(m)) 

# Test auf Nachfolger
2 in G[1]   
1 in G[2]   

# Ausgangsgrad in O(1)
u = 1
outdeg = len(G[u])

# Eingangsgrad in O(m)
u = 2
indeg = sum(1 for v in range(len(G)) if u in G[v])

