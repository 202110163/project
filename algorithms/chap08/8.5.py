INF = 9999

def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0  # 선택된 정점의 초기 거리를 0으로 설정

    for i in range(vsize):
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(f"{vertex[u]}:{dist}")  # dist 리스트의 상태를 출력

        for v in range(vsize):
            if adj[u][v] is not None:
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [
    [None, 29, None, None, None, 10, None],
    [29, None, 16, None, None, None, 15],
    [None, 16, None, 12, None, None, None],
    [None, None, 12, None, 22, None, 18],
    [None, None, None, 22, None, 27, 25],
    [10, None, None, None, 27, None, None],
    [None, 15, None, 18, 25, None, None]
]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)
