class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children
        
list = Node('A', [Node('C', [Node('D')]), Node('Z', [Node('X', [Node('M')])])])


def longest_leaf(node):
    if not node or len(node.children) == 0:
        return 1
    
    distances = []
    
    for child in node.children:
        distances.append(longest_leaf(child))
    
    return 1 + max(distances)
    
print(longest_leaf(list))