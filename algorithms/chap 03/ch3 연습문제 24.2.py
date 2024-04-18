from collections import deque

def bfs(adjMat, vertex, start):
    visited = [False] * len(vertex)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(vertex[v], end=' ')

        for i in range(len(adjMat[v])):
            if adjMat[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

start_node_index = 0 
print("BFS:", end=" ")
bfs(adjMat, vertex, start_node_index)
