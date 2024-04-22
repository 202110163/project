def topological_sort(graph):
    indeg = {}
    for v in graph:
        indeg[v] = 0
    for v in graph:
        for u in graph[v]:
            indeg[u] += 1

    vlist = []
    for v in graph:
        if indeg[v] == 0:
            vlist.append(v)

    sorted_elements = []
    while vlist:
        v = vlist.pop()
        sorted_elements.append(v)

        for u in graph[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                vlist.append(u)

    print(' '.join(sorted_elements))

mygraph = {
    "A": {"C", "D"},
    "B": {"D", "E"},
    "C": {"D", "F"},
    "D": {"F"},
    "E": {"F"},
    "F": {}
}
print('topological_sort:')
topological_sort(mygraph)
print()