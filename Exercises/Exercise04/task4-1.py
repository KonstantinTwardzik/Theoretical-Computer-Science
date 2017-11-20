'''
Created on 27.10.2017

@author: Konstantin
'''

# 4.1
def psi (x):
    y = (x+1)
    while (x < y):
        y = (x+1)
    return y
        
# 4.2
def prodZ(x,y):
    z = 0
    if (x < 0):
        x = (0 - x)
        y = (0 - y)
    for i in range(0,x):
        z = (z + y)
    return z

def divZ(x,y):
    if (y != 0):
        if (y < 0):
            y = (0 - y)
            x = (0 - x)
        z = 0
        if (x < 0):
            z = x
        while (prodZ(y,z) <= x):
            z = (z+1)
        z = (z - 1)
    return z 

def modZ(x,y):
    if ((x >= 0) and (y >= 0)):
        return (x - (y * divZ(x, y)))

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
    z = 0
    y = 0
    x = 1
    if (n >= 0):
        while(n >= y):
            if (teil(x) == 2):
                z = x
                y = (y + 1)
            x = (x + 1)
    else: 
        z = 2
    return z


# 4.4
def fakul1(x):
    result = 1
    y = 1
    for y in range(x):
        z = 1
        help = result
        for z in range (y):
            result = (result + help)
            z = (z + 1)
        y = (y + 1)    
    return result

def fakul2(x):
    if (x == 0):
        result = 1
    elif (x == 1):
        result = 1
    elif (x == 2):
        result = 2
    else:
        result =  x * fakul2(x-1)  
    return result      

def fakul3(x):
    result = 1
    y = 1
    if(x >= 0):
        while(x > y):
            z = 1
            help = result
            while (y >= z):
                result = (result + help)
                z = (z + 1)
            y = (y + 1)    
    else:
        result = f
    return result        
    
    
#4.5
            
def f3(x):
    y=0
    i=0
    for i in range (0,x):
        y = (y + x)
    return y

def f4(x):
    i=0
    for i in range (0,x):
        x = (x + 2)
    return x

        
#4.7 

def f7(x,y):
    z = 1
    if ((x>0) and (y>0)):
        z = 0
        for i in range(0,x):
            z = (z + f7(x,(y-1)))
    return z
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        