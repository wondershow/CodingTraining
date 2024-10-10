class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        
        When we are doing the preorder traversal of a BST using a stack,
        1. The stack path is always a monotoically decreasing stack. 
        2. The stack pop order should be always nondecreasing or increasing.
        3. The preorder is the stack push order. 
        So the sliding max of 2 must be smaller than 3 (pop first then push the current item). We use this to determine if it is the correct BST preorder
        """
        stack, max_seen = [], 0
        for val in preorder:
            if val <= max_seen:
                return False
            while stack and stack[-1] < val:
                max_seen = max(max_seen, stack.pop())
            stack.append(val)
        return True
