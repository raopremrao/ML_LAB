# AO* Algorithm 
graph = {    
    'A': [('B', 1), ('C', 1), ('D', 1)],    
    'B': [('E', 1), ('F', 1)],    
    'C': [('G', 1), ('H', 1), ('I', 1)],    
    'D': [('J', 1)],    
    'E': [],    
    'F': [],    
    'G': [],    
    'H': [],    
    'I': [],    
    'J': [] 
}

# Heuristic values from the diagram 
h = {    
     'A': 5,    
     'B': 5,    
     'C': 3,    
     'D': 4,    
     'E': 10,    
     'F': 11,    
     'G': 3,    
     'H': 0,    
     'I': 0,    
     'J': 1 
    }

def ao_star(start, goal):    
    current = start    
    path = [current]    
    total_cost = 0    
    
    while current != goal:        
        if current not in graph or len(graph[current]) == 0:            
            break        
        
        # Select the child with minimum f(n)        
        best_node = None        
        best_cost = float('inf')       
        edge_cost = 0
         
        for child, cost in graph[current]:            
            f = cost + h[child]
            
            if f < best_cost:                
                best_cost = f                
                best_node = child                
                edge_cost = cost        

        # Update current node and path outside the for loop
        if best_node is None:
            break

        current = best_node        
        path.append(current)        
        total_cost += edge_cost   
                
    print("AO* Path:")
    print(" -> ".join(path))    
    print("Total Cost:", total_cost)
        
        
# Start node and goal node 
ao_star('A', 'H')