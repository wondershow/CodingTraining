#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        This is a simple heap question. But I made 4 mistakes(all trivial)
        1. Failed to add 'heap' as argument in the 'heappush' method
        2. When adding node into heap, need to add a tiebreaker since we cant compare nodes. (I used a sequence)
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap, dummy = [], ListNode(0)
        tail, seq = dummy, 0
        for n in lists:
            if n:
                heappush(heap, [n.val, seq, n])
                seq += 1
                
        while heap:
            _, _, node = heappop(heap)
            tail.next = node
            if node.next:
                heappush(heap, [node.next.val, seq, node.next])
                seq += 1
            tail = tail.next
        
        return dummy.next
