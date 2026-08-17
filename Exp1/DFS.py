graph = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F'],
         'C': [],
         'D': ['G'],
         'E': [],
         'F': [],
         'G': []       
}

visited = set ()
def dfs(graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs (graph, neighbor)
print("DFS Traversal starting from node A:")
dfs(graph, 'A')