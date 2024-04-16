import queue
def bfs(graph, start):
    visited = { start }
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v, end= " ")
        nbr = sorted(graph[v] - visited)
        for u in nbr:
            visited.add(u)
            que.put(u)

mygraph =  {"A":{"B", "C"}, "B":{"A", "D"}, "C":{"A", "D", "E"}, "D":{"B", "C", "F"}, "E":{"C", "G", "H"}, "F":{"D"}, "G":{"E", "H"}, "H":{"E", "G"}}

print('BFS : ', end= " ")
bfs(mygraph, "A")
print()