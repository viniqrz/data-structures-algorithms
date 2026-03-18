class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

A = Node('A')
B = Node('B')
C = Node('C')
A.next = B
B.next = C
C.next = B
listA = A
# listB = Node('A', Node('B', Node('C', Node('D'))))


def detect_cycle_in_linked_list(head):
    node = head
    # while node:
    #     print(node.val)
    #     node = node.next
        
        
    slow = head
    fast = head

    # Loop that runs while fast and slow pointer are not
    # None and not equal
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If fast and slow pointer points to the same node,
        # then the cycle is detected
        if slow.val == fast.val:
            return True
    return False
    
    # fast = head
    # slow = head
    
    # while fast and slow and fast.next:
    #     fast = fast.next.next
    #     slow = slow.next
    
    #     if (fast.val == slow.val):
    #         return True

    # return False

print(detect_cycle_in_linked_list(listA))
# print(detect_cycle_in_linked_list(listB))