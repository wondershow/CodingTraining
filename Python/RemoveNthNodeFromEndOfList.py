# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = tail = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n):
            tail = tail.next
        while tail.next:
            tail = tail.next
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
        
