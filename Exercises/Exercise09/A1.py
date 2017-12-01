'''
Created on 01.12.2017

@author: Konstantin
'''
# Definition des NEA A
# beachten Sie den Unterschied bei delta

def define_nea_A(): 
    Q = {'start', 0, 1, 2, 'akzeptiert'}  # Zustandsmenge
    Sigma = {'0', '1', '2'}  # Alphabet    
    delta = {}  # leeres Dictionary
    
    delta['start', '0'] = {'start', 0}  # value = Menge (!) der Folgezustaende
    delta['start', '1'] = {'start', 1}
    delta['start', '2'] = {'start', 2}
    delta[0, '0'] = {0, 'akzeptiert'}   
    delta[0, '1'] = {0}
    delta[0, '2'] = {0}
    delta[1, '0'] = {1}    
    delta[1, '1'] = {1, 'akzeptiert'}
    delta[1, '2'] = {1}
    delta[2, '0'] = {2}
    delta[2, '1'] = {2}
    delta[2, '2'] = {2, 'akzeptiert'}
    delta['akzeptiert', '0'] = set()
    delta['akzeptiert', '1'] = set()
    delta['akzeptiert', '2'] = set()

    F = {'akzeptiert'}  # Menge akz. Zustaende     
    A = [Q, Sigma, delta, 'start', F]  # Automatentupel inkl Startzustand 
    return A

A = define_nea_A()


# erweiterte Ueberfuehrungsfunktion fuer NEAs
def delta_dach_nea(delta, q, w):
    R = {q}  # (IA)
    for a in w:  # (IS)
        R = {q for p in R  # fuer alle p aus R_alt 
               for q in delta[p, a]}  # die Mengen der Folgezustaende vereinigen    
    return R

# beliebigen NEA laufen lassen
def run_nea(A, w): 
    [Q, Sigma, delta, q0, F] = A  # unpacking in O(1)
    return (delta_dach_nea(delta, q0, w) & F) != set()  # Test in O(#Q)           


# Verwendung
run_nea(A, '0111')
run_nea(A, '01110')
