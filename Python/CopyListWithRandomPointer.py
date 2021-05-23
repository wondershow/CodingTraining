"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    A tricky method. 
    
    A->B->C
    
    A->A'->B->B'->C->C'
    
    Mistakes made:
    when assigning random pointer, failed to check if the origin node's random pointer might be empty.
    """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p = head
        while p:
            p_next = p.next
            new_node = Node(p.val)
            new_node.next = p_next
            p.next = new_node
            p = p_next
        
        res = head.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
            
        p = head
        while p:
            p_next = p.next.next
            if p_next:
                p.next.next = p_next.next
            else:
                p.next.next = None
            p.next = p_next
            p = p_next
        
        return res
