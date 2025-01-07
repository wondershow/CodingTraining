class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def search(i, path, res):
            """
            Basic back tracking. At each poistion, there are 2 options, add or not add.
            """
            if len(path) == k:
                res.append(path[:])
                return
            if i > n or len(path) + (n - i + 1) < k:
                return
            path.append(i)
            search(i + 1, path, res)
            path.pop()
            search(i + 1, path, res)
        
        res, path = [], []
        search(1, path, res)
        return res
