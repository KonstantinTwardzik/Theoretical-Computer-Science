
# Ihre Loesung fuer Aufgabe 18

final={1:'one', 2:'two', 3:'three', 4:'four',       \
   5:'five', 6:'six', 7:'seven', 8:'eight',     \
   9:'nine', 10:'ten', 11:'eleven', 12:'twelve',\
   13:'thirteen', 14:'fourteen', 15:'fifteen',       \
   16:'sixteen', 17:'seventeen', 18:'eighteen',      \
   19:'nineteen'}
tenth={2:'twenty', 3:'thirty', 4:'forty', \
   5:'fifty', 6:'sixty', 7:'seventy',  \
   8:'eighty', 9:'ninety'}

# for 1 <= k <= 999
def int_to_str(k):

# TODO


letters = 0
for k in range(1,1000):
    letters += len(int_to_str(k))
print(letters+len('onethousand'))      


