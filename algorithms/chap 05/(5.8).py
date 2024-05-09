import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) #3장 113p

def strip_closest(P, d):
    n = len(P)
    d_min = d

    for i in range(n):
        j = i + 1
        while j < n and P[j][1] - P[i][1] < d_min: 
            dij = distance(P[i], P[j])
            if dij < d_min:
                d_min = dij
            j += 1
    return d_min

P = [(2,6),(4,7),(4,1),(5,1),(3,2)]
P.sort(key=lambda point: point[1])  
print("띠 영역내에서 d보다 작은 최근접쌍의 거리 찾기:", strip_closest(P, len(P)))