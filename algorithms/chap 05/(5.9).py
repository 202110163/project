import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def strip_closest(P, d):
    n = len(P)
    d_min = d
    P.sort(key = lambda point: point[1])

    for i in range(n):
        j = i + 1
        while j < n and (P[j][1] - P[i][1]) < d_min:
            dij = distance(P[i], P[j])
            if dij < d_min :
                d_min = dij
            j += 1
    return d_min

def closest_pair_dist(P, n):
    if n <= 3:
        return closest_pair(P)
    
    mid = n // 2
    mid_x = P[mid][0]

    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n-mid)
    d = min(dl, dr)

    Pm = []
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])

    ds = strip_closest(Pm, d)
    return ds

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p.sort(key = lambda point: point[0])
print("가장 가까운 두 점의 거리", closest_pair_dist(p, len(p)))