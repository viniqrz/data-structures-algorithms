def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):  # Handle potential missing keys
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)  # Add to stack after all descendants are processed

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1] # Reverse the stack for the correct topological order

# Example Usage:
graph = {
    'A': ['D'],
    'B': ['D'],
    'C': ['A', 'B'],
    'D': ['G', 'H'],
    'E': ['F'],
    'F': ['H'],
    'G': [],
    'H': []
}

sorted_order = topological_sort_dfs(graph)
print(f"Topological Sort Order: {sorted_order}")