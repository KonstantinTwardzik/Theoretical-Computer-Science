'''
Created on 24.11.2017

@author: Konstantin
'''
def define_dea_A_v():
    Q = {0, 1, 2, 3, 4, 5, 6, 7}
    Sigma = {"a", "b", "c"}
    delta = {}
    
    delta[0, "a"] = 1
    delta[0, "b"] = 0
    delta[0, "c"] = 0
    delta[1, "a"] = 1
    delta[1, "b"] = 0
    delta[1, "c"] = 2
    delta[2, "a"] = 1
    delta[2, "b"] = 3
    delta[2, "c"] = 0
    delta[3, "a"] = 4
    delta[3, "b"] = 0
    delta[3, "c"] = 0
    delta[4, "a"] = 1
    delta[4, "b"] = 0
    delta[4, "c"] = 5
    delta[5, "a"] = 6
    delta[5, "b"] = 0
    delta[5, "c"] = 0
    delta[6, "a"] = 1
    delta[6, "b"] = 0
    delta[6, "c"] = 7
    delta[7, "a"] = 7
    delta[7, "b"] = 7
    delta[7, "c"] = 7
    
    F = {7}
    A = [Q, Sigma, delta, 0 , F]
    return A
    
def delta_dach_dea(delta, q, w): 
    for a in w:             
        q = delta[q, a]     
    return q

def run_dea(A, w): 
    [Q, Sigma, delta, q0, F] = A                
    return delta_dach_dea(delta, q0, w) in F  
    
A_v = define_dea_A_v()
run_dea(A_v, "abcbcbcbacbacacacacbcb") #true
run_dea(A_v, "abcbcbcbacbacbcacbcb")#false