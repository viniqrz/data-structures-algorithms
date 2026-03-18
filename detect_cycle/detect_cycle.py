
class Node:
    def __init__(self, val, children: list = []):
        self.val = val
        self.children = children

visited = set()

def detect_cycle(node):
    if not node:
        return False
    
    if node.val in visited:
        return True
    
    visited.add(node.val)
    
    for child in node.children:
        if detect_cycle(child):
            return True

    return False


#   A
#  / \
# B   C
#  \ /
#  Z

print(detect_cycle(Node('A', [Node('B', [Node('Z')]), Node('C', [])])))# Should return True
