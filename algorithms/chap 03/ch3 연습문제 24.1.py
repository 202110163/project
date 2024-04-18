def dfs(adjMat, vertex, start, visited):
    visited[start] = True
    print(vertex[start], end=' ')

    for i in range(len(adjMat[start])):
        if adjMat[start][i] == 1 and not visited[i]:
            dfs(adjMat, vertex, i, visited)

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

visited = [False] * len(vertex)

start_node_index = 0  
print("DFS:", end=" ")
dfs(adjMat, vertex, start_node_index, visited)
