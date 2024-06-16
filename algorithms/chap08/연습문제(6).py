import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)] 

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)

        if current in visited:
            continue

        visited.add(current)
        if prev is not None:
            mst.append((prev, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst

graph = {
    'A': [('C', 4), ('B', 7), ('E', 2)],
    'B': [('A', 7), ('D', 3), ('E', 4)],
    'C': [('A', 4), ('D', 6), ('E', 3)],
    'D': [('B', 3), ('C', 6), ('E', 5)],
    'E': [('A', 2), ('B', 4), ('C', 3), ('D', 5)]
}

start_vertex = 'A'
mst = prim(graph, start_vertex)

for edge in mst:
    print(edge)
