# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def get_mid(head):
            slow = dummy = ListNode(0)
            dummy.next = head
            fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return None if slow == dummy else slow
        
        def merge_sort(head):
            pre_mid = get_mid(head)
            left = head
            
            # We only have one element in the input list
            if not pre_mid:
                return head
            
            
            right = pre_mid.next
            
            # break the input list into 2 sublists
            pre_mid.next = None
            
            left = merge_sort(left)
            right = merge_sort(right)
            
            tail = dummy = ListNode(0)
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            else:
                tail.next = right
            return dummy.next
        
        return merge_sort(head)
