
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#        A
#       / \
#      B   C
#     / \   \
#    D   E   F


def dfs(graph: dict, node):
    if node not in graph.keys():
        return
    
    print(node)
    
    for child in graph[node]:
        dfs(graph, child)
    
print(dfs(graph, 'A'))
