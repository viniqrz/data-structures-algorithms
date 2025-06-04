from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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

print(bfs(graph, 'A'))

def bfs_2(graph: dict, start_node):
    visited = set()
    queue = deque([list(graph.keys())[0]])
    visited.add(start_node)
    res = []
    
    while queue:
        node = queue.popleft()
        res.append(node)
        for child in graph[node]:
            if child not in visited:
                visited.add(node)
                queue.append(child)

    print(res)

    return res

def unit_tests():
    
    def case_1():
        bfs_2(graph, 'A')
    case_1()
        
    def case_2():
        pass
    case_2()

    
unit_tests()
        
    