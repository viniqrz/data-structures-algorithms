class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
list = Node('A', Node('B', Node('C', Node('D'))))


def reverse_linked_list(head):
    curr = head
    prev = None
    while curr:
        print(curr.val)
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    node = prev
    while node:
        print(node.val)
        node = node.next

reverse_linked_list(list)