#         self.next = next
class Solution:
    """
    Find the middle point and start of right half.
    Then do the compare. 
    """
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow.next is the start of right half
        slow = slow.next
        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next
        while stack:
            if stack[-1].val != head.val:
                return False
            head = head.next
            stack.pop()
        return True
