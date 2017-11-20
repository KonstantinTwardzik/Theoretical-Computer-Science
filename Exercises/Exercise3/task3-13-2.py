'''
Created on 23.10.2017

@author: Konstantin
'''

sprache = {"Hallo", "wie", "gehts"}
k = 3
konkatenierteSprache = {""}

def concat_k(L,K):
    helper = L.copy()
    helper2 = L.copy()
    if K == 0:
        return ""
    else:
        for x in L:
            for y in helper2:
                helper.add(x+y)
                
        concat_k(L,K-1)
        return helper




konkatenierteSprache = concat_k(sprache, k)   
print(konkatenierteSprache)
