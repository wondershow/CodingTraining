"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        #new_head = Node(head.val)
        
        cur = head
        while cur:
            new_node = Node(cur.val)
            next_node = cur.next
            new_node.next = next_node
            cur.next = new_node
            cur = next_node
            
        new_head = head.next
        cur = head
        while cur:
            cur_next = cur.next.next
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur_next
        
        cur = new_head
        while cur.next:
            cur_next = cur.next.next
            cur.next = cur_next
            cur = cur_next
        
        return new_head
