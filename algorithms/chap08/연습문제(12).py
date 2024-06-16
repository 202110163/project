class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    vertices = list(graph.keys())
    edges = []

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    
    edges.sort()
    disjoint_set = DisjointSet(vertices)
    mst = []
    
    for weight, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append((u, v, weight))
    
    return mst

graph = {
    'A': [('C', 4), ('B', 7), ('E', 2)],
    'B': [('A', 7), ('D', 3), ('E', 4)],
    'C': [('A', 4), ('D', 6), ('E', 3)],
    'D': [('B', 3), ('C', 6), ('E', 5)],
    'E': [('A', 2), ('B', 4), ('C', 3), ('D', 5)]
}

mst = kruskal(graph)

for edge in mst:
    print(edge)
