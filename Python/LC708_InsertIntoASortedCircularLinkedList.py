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


    def insert2(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        # 1. When it is empty
        if not head:
            newNode.next = newNode
            return newNode

        # 2. When there is only 1 node
        if head.next == head:
            head.next, newNode.next = newNode, head
            return head


        # 3. Find the smallest node and pre
        cur, pre = head, None
        while cur:
            # When the cur val is smaller than pre, meanning we hit the last element of the sorted list
            # Note the exit condition should be at the very end.
            if pre and cur.val < pre.val:
                break
            cur, pre = cur.next, cur
            if cur == head:
                break
        
        # 4. if the insertval smaller than the smallest or larger than pre  insert between last and first
        if insertVal < cur.val or insertVal > pre.val:
            newNode.next, pre.next = cur, newNode
            return head

        # 5. if the value is between current and next, insert
        while cur:
            if cur.val <= insertVal <= cur.next.val:
                newNode.next = cur.next
                cur.next = newNode
                break
            cur = cur.next
