# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def reverse(head):
            dummy = ListNode(0)
            tail = head
            while head:
                next_head = head.next
                head.next = dummy.next
                dummy.next = head
                head = next_head
            return [dummy.next, tail]
        
        def get_left_right(dummy, left, right):
            cur = dummy
            pre_left, left_node, right_node, after_right = None, None, None, None
            count = 0
            while cur:
                if count == left - 1:
                    pre_left = cur
                if count == left:
                    left_node = cur
                if count == right:
                    right_node = cur
                    after_right = cur.next
                    break
                count += 1
                cur = cur.next
            return [pre_left, left_node, right_node, after_right]
        
        dummy = ListNode(0)
        dummy.next = head
        pre_left, left_node, right_node, after_right = get_left_right(dummy, left, right)
        right_node.next = None
        new_head, new_tail = reverse(left_node)
        pre_left.next = new_head
        new_tail.next = after_right
        return dummy.next
