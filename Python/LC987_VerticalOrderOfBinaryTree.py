class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def helper(root, x, y, level_lsit):
            if not root:
                return
            level_lsit[x].append([y, root.val])
            helper(root.left, x - 1, y + 1, level_lsit)
            helper(root.right, x + 1, y + 1, level_lsit)
        
        level_list = defaultdict(list)
        helper(root, 0, 0, level_list)
        res = []
        for key in sorted(level_list.keys()):
            item = level_list[key]
            item.sort()
            res.append([a[1] for a in item])
        return res
