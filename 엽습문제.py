import heapq

from hello2 import inc
freg = [1,5,2,7,9,20,19]
n = len(freg)
h=[]
for i in range(n):
    heapq.heappush(h, (freg[i]))
    
    inc = []
    for i in range(n):
        inc.append(heapq.heappop(h))
        
print(freg)
print(inc)