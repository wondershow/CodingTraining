"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    This is the one pass solution. 
    consider 3 cases:
    1. insertVal out of range
    2. all values of linkedlist are same
    3. regular case
    
    edge case when head is None
    need to make new_node circular as well
    """
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        new_node.next = new_node
        if not head:
            return new_node
        cur, pre = head.next, head
        while cur.next != head.next:
            if pre.val <= insertVal <= cur.val and pre.val != cur.val:
                pre.next = new_node
                new_node.next = cur
                return head
            elif pre.val > cur.val:
                if insertVal <= cur.val or insertVal >= pre.val:
                    pre.next = new_node
                    new_node.next = cur
                    return head
            cur = cur.next
            pre = pre.next
        pre.next = new_node
        new_node.next = cur
        return head
