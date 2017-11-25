'''
Created on 22.11.2017

@author: Konstantin
'''
def define_dea_A4():
    Q = {0, 1, 2, 3, 4, 5, 6, 7}
    Sigma = {"a", "b", "c"}
    delta = {}
    
    delta[0, "a"] = 1
    delta[0, "b"] = 7
    delta[0, "c"] = 3
    delta[1, "a"] = 2
    delta[1, "b"] = 7
    delta[1, "c"] = 7
    delta[2, "a"] = 1
    delta[2, "b"] = 7
    delta[2, "c"] = 3
    delta[3, "a"] = 4
    delta[3, "b"] = 7
    delta[3, "c"] = 7
    delta[4, "a"] = 7
    delta[4, "b"] = 7
    delta[4, "c"] = 5
    delta[5, "a"] = 6
    delta[5, "b"] = 7
    delta[5, "c"] = 7
    delta[6, "a"] = 7
    delta[6, "b"] = 7
    delta[6, "c"] = 3
    delta[7, "a"] = 7
    delta[7, "b"] = 7
    delta[7, "c"] = 7
    
    F = {0, 2, 6}
    A = [Q, Sigma, delta, 0, F]
    return A
       
def delta_dach_dea(delta, q, w): 
    for a in w:             
        q = delta[q, a]     
    return q

def run_dea(A, w): 
    [Q, Sigma, delta, q0, F] = A                
    return delta_dach_dea(delta, q0, w) in F             

A1 = define_dea_A4()
run_dea(A1, "c")

    