
# Referenz auf 1
x = 1
# wird umgebogen auf 'a'
x = 'a'

# a und b zeigen beide auf dasselbe Objekt
a = [1,2,3]
b = a           

c = [ b, 3 ]
a[0]=0
c

# Slicing erzeugt flache Kopien
foo = c[:]
a[0]=1
foo

# call by object reference
def f(B, w):
    B.add(2)
    w += ' world'
    print(w)

A = {0,1}       # mutable
v = 'hello'     # immutable
f(A,v)
print(A,v)


from copy import deepcopy
l = deepcopy(foo)


# Hilfesystem
help(deepcopy)



