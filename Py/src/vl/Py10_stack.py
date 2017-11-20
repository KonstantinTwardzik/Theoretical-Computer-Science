
###################################################
# LIFO: Stack S als Liste
#
S = [10, 11, 12, 13] 

# push
S.append(14)
S.append('a')

# top
S[-1]

# pop
S.pop()
S[-1]
S.pop()

# Anzahl Elemente auf Stack
len(S)



###################################################
# FIFO: Queue Q 
# 
from collections import deque

Q = deque([1,2,3]) 

# enqueue (rechts anhaengen)
Q.append(4)
Q.append('a')

# peek
Q[0]
Q[-1]
Q

# dequeue (links herausnehmen)
Q.popleft()
Q.popleft()

# peek
Q[0]
Q[-1]

# Anzahl Elemente in der Queue
len(Q)


###################################################
# Min Priority Queue P (heap-Implementierung)
# 
from heapq import heappush, heappop, heapify

P = []

# insert
heappush(P,3)
heappush(P,1)
heappush(P,4)
heappush(P,2)

P

# peek
P[0]

# get next
while P:
    x=heappop(P)
    print(x)
heappop(P)  # index error


# heapsort
a = [3,1,2,6,3,4]
heapify(a)
while a:
    print(heappop(a))



