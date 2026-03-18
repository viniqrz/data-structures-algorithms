def tsp(graph):
    nodes = list(graph.keys())
    total_nodes = len(nodes)
    
    def dfs(node, distance=0, path=[]):
        # 1. If we hit a cycle before visiting everyone, it's an invalid path.
        # We return infinity so min() ignores it.
        if node in path:
            return float('inf')
            
        path.append(node)
        
        # 2. Classical TSP Base Case: Visited every node, now go home!
        if len(path) == total_nodes:
            start_node = path[0]
            current_node = node
            
            # Look for the edge connecting the last node back to the start
            for neighbor, weight in graph.get(current_node, []):
                if neighbor == start_node:
                    return distance + weight
            
            # If there is no road back to the start, it's an invalid loop
            return float('inf')
    
        distances = [float('inf')]
    
        # 3. Explore neighbors
        # (Using .get(node, []) prevents TypeError if a node has no outgoing edges)
        for child, child_distance in graph.get(node, []):
            distances.append(dfs(child, distance + child_distance, path.copy()))
        
        return min(distances)

    distances = [float('inf')]
    
    for node in nodes:
        distances.append(dfs(node, 0, []))
        
    shortest = min(distances)
    
    # Return -1 if it's impossible to reach all nodes
    return shortest if shortest != float('inf') else -1


# --- Standardized Test Graph ---
graph = { 
    'A': [('B', 2), ('C', 1), ('D', 2)], 
    'B': [('A', 2), ('C', 3)], 
    'C': [('D', 1), ('A', 1), ('B', 3)], 
    'D': [('C', 1), ('A', 2)] 
}

print(f"Shortest path distance: {tsp(graph)}")