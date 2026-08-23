import heapq

# Graph: node -> (neighbour, cost)
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic values from the diagram
h = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 2,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 3,
    'J': 0
}

def a_star(start, goal):

    # Priority queue: (f, g, node, path)
    queue = [(h[start], 0, start, [start])]

    visited = set()
    while queue:
        f, g, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            return
        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbour]
                heapq.heappush(
                    queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )
# Start A, Goal J
a_star('A', 'J')