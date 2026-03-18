class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children
        
list = Node('A', [Node('C', [Node('D')]), Node('Z', [Node('X', [Node('M')])])])


def shortest_path():
    # // bfs
    pass