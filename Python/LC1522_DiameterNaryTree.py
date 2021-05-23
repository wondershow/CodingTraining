class Solution:
    """
    The key is maintain a best and subbest pair when doing recursive calls on child
    """
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(root):
            if not root:
                return [float("-inf"), 0]
            local_max, longest_child, sub_best = 0, 0, 0
            for child in root.children:
                child_max, child_depth = dfs(child)
                local_max = max(local_max, child_max)
                if child_depth > longest_child:
                    sub_best = longest_child 
                    longest_child = child_depth
                elif child_depth > sub_best:
                    sub_best = child_depth
            local_max = max(local_max, sub_best +  longest_child)
            return [local_max, 1 + longest_child]
        return dfs(root)[0]
