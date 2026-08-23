graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited_node = []
queue_node = []
def bfs(visited_node, graph, snode):
    visited_node.append(snode)
    queue_node.append(snode)
    print()
    print("Result: ")
    while queue_node:
        s = queue_node.pop(0)
        print(s, end=" ")
        for neighbor in graph[s]:
            if neighbor not in visited_node:
                visited_node.append(neighbor)
                queue_node.append(neighbor)
snode = input("Enter Starting node: ")
bfs(visited_node, graph, snode)    