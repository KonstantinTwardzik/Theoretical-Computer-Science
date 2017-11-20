

###########################################################
# Graphen mit Kantenkosten

# zusaetzliche Eingabe: c(e) fuer alle e=(u,v) aus E
# 
# Dictionary G[u] enthaelt alle v:c(e) 

def define_G3():
    G = [   {1:2},              # Nachfolger fuer Knoten 0
            {0:2, 2:5, 3:7},    # Nachfolger fuer Knoten 1 
            {1:5, 3:6},         # Nachfolger fuer Knoten 2
            {1:7, 2:6},         # Nachfolger fuer Knoten 3
        ]
    return G


# Verwendung
G = define_G3()

# Test auf Nachbarschaft wie ueblich
2 in G[1]   
0 in G[3]   

# Kantenkosten
G[2][1]

# alle Nachbarn mit Kantenkosten
v = 2
for w in G[v]:
    print('e=(',v,',',w,') mit c(e)=', G[v][w])

# alternativ:
for w,c in G[v].items():
    print('e=(',v,',',w,') mit c(e)=', c)

