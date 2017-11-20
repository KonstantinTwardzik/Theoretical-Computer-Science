

# verwendet bin_str(n) aus Uebung
from ueb.lek03.aufg15_bin_str import bin_str

# x besteht aus 100 Bits 1111...1
x = pow(2,100)-1

len(bin_str(x))  # n = |x| = 100

z = 0 
for i in range(0, x):
    z = z + 1

# z ist die ausgefuehrte Iterationszahl
# Abbruch mit crtl-c
