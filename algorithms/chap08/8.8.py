INF = float('inf')

def getMinVertex(dist, found):
    minv = INF
    minidx = -1
    for i in range(len(dist)):
        if not found[i] and dist[i] < minv:
            minv = dist[i]
            minidx = i
    return minidx

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    
    for i in range(vsize - 1):
        print("Step%2d:" % (i + 1), dist)
        u = getMinVertex(dist, found)
        found[u] = True
        
        for w in range(vsize):
            if not found[w] and adj[u][w] != INF:
                if dist[u] + adj[u][w] < dist[w]:
                   dist[w] = dist[u] + adj[u][w]
                   path[w] = u

    return path

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [0, 7, INF, INF, 3, 10, INF],
    [7, 0, 4, 10, 2, 6, INF],
    [INF, 4, 0, 2, INF, INF, INF],
    [INF, 10, 2, 0, 11, 9, 4],
    [3, 2, INF, 11, 0, 13, 5],
    [10, 6, INF, 9, 13, 0, INF],
    [INF, INF, INF, 4, 5, INF, 0]
]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)):
    if end != start:
        print("[최단 경로: %s->%s] %s" % (vertex[start], vertex[end], vertex[end]), end='')
        trace = end
        while path[trace] != start:
            print(" <- %s" % vertex[path[trace]], end='')
            trace = path[trace]
        print(" <- %s" % vertex[start])
