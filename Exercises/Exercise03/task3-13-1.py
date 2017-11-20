sprache1 = {"ab","bc","c"}
sprache2 = {"def","esd","f"}
konkatenierteSprache = {""}

def concat (L1, L2):
    for x in L1:
        for y in L2:
            konkatenierteSprache.add(x+y)

concat(sprache1,sprache2)
print(konkatenierteSprache)