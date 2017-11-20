'''
Created on 08.11.2017

@author: Konstantin
'''

# 5.2
def  fünfzwei (x):
    if ((((x == 8) or (x == 2197)) or (x == 10071))):
        x = x 
    else:
        x = z
    return x
    
# 5.3
def prodZ(x, y):
    z = 0
    if (x < 0):
        x = (0 - x)
        y = (0 - y)
    for i in range(0, x):
        z = (z + y)
    return z

def fünfdrei (x):
    i = 0
    z = 1 
    if (x != 1):
        decision = False
        while (i < x):
            z = prodZ(z, 2)
            if (x == z):
                decision = True
                i = x 
            else:
                i = (i + 1)
    else:
        decision = True
    return decision

# 5.4
def prodZ(x, y):
    z = 0
    if (x < 0):
        x = (0 - x)
        y = (0 - y)
    for i in range(0, x):
        z = (z + y)
    return z

def divZ(x, y):
    if (y != 0):
        if (y < 0):
            y = (0 - y)
            x = (0 - x)
        z = 0
        if (x < 0):
            z = x
        while (prodZ(y, z) <= x):
            z = (z + 1)
        z = (z - 1)
    return z 

def modZ(x, y):
        return (x - (prodZ(y,divZ(x, y))))

def teil(x):
    z = 0
    y = 1
    if (x >= 1): 
        while(y <= x):
            if (modZ(x,y) == 0):
                z = (z+1)
            y = (y + 1)
    return z

def prim(n):
    i = 3
    primzahl = 0
    while(primzahl < n):
        if (teil(i) == 2):
            primzahl = (primzahl + 1)
        i = (i + 1)
    return (i-1)

def fünfvier (n):
    i1 = 0
    while(i1 < n):
        i2 = 0
        x = prim(i1)
        while (i2 <= i1):
            y = prim(i2)
            if (n == (x+y)):
                i2 = n
                i1 = n
            i2 = (i2+1)
        i1 = i1+1
    return x,y
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
