class Solution:
    """
    My understanding of this template: when helper is given a partial result of permutation, lets use 
    1,2,3,4 as an example. When a partial result (path  parameter is given, ) the helper only does one thing, 
    it picks one element from the available set, and pass this set to next level of helper.
    How to tag is an element is used or not? We use a set `used` to contain all elements used in the current subset.
  

    The time complexity is O(N!)
    
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        used, path, res = set(), [], []

        def helper(path, res, used):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    helper(path, res, used)
                    path.pop()
                    used.remove(nums[i])

        helper(path, res, used)
        return res
