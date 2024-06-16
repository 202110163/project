INF = float('inf')

def getMinVertex(dist, found):
    minv = INF
    minidx = -1
    for i in range(len(dist)):
        if not found[i] and dist[i] < minv:
            minv = dist[i]
            minidx = i
    return minidx

def shortest_path_dijkstra(vertex, adj, start):
    vsize = len(vertex)
    dist = [INF] * vsize
    dist[start] = 0
    path = [-1] * vsize
    found = [False] * vsize
    
    for _ in range(vsize):
        u = getMinVertex(dist, found)
        found[u] = True
        
        for w in range(vsize):
            if not found[w] and adj[u][w] != INF:
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
    
    return path, dist

def print_shortest_paths(vertex, start, path, dist):
    print("src -> dst     dist      path")
    for end in range(len(vertex)):
        if end != start:
            print(f"{vertex[start]}->{vertex[end]:5}        {dist[end]:5}     ", end='')
            if dist[end] == INF:
                print("NO PATH")
            else:
                # 경로 역추적
                path_trace = []
                trace = end
                while trace != -1:
                    path_trace.append(vertex[trace])
                    trace = path[trace]
                path_trace.reverse()  # 역순으로 출력되어야 올바른 경로가 됩니다.
                print(" ".join(map(str, path_trace)))

# 그래프 정의 (가중치 변경)
vertex = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
weight = [
    [0, 4, INF, INF, 21, INF, 14, 8, INF],
    [4, 0, INF, INF, INF, INF, 9, 6, 15],
    [INF, INF, 0, 2, INF, INF, INF, 7, 11],
    [INF, INF, 2, 0, 11, 9, INF, INF, INF],
    [21, INF, INF, 11, 0, 13, 5, INF, 17],
    [INF, INF, INF, 9, 13, 0, 8, 7, 14],
    [14, 9, INF, INF, 5, 8, 0, 12, INF],
    [8, 6, 7, INF, INF, 7, 12, 0, 10],
    [INF, 15, 11, INF, 17, 14, INF, 10, 0]
]

# 가중치 수정
weight[0][4] = 21
weight[4][5] = INF  # 4에서 5로 가는 경로를 없애기 위해 무한대로 설정
weight[5][4] = INF  # 5에서 4로 가는 경로 역시 없애기 위해 무한대로 설정
weight[5][6] = 8
weight[0][7] = 8
weight[7][8] = 10

# 최단 경로 계산 및 출력
start = 0
path, dist = shortest_path_dijkstra(vertex, weight, start)
print_shortest_paths(vertex, start, path, dist)
