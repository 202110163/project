import math
import sys
INF = sys.maxsize

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closet_pair(p):
    n=len(p)
    mindist=float(INF)
    for i in range(n-1):
        for j in range(i+1, n):
            dist=distance(p[i], p[j])
            if dist < mindist:
                mindist=dist
    return mindist

p=[(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
print("최근접 거리", closet_pair(p))