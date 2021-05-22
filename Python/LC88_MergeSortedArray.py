class Solution:
    """
    2 mistakes made:
    1. when doing the comparison it is ">=" not "<=" since we are picking larger elements to "append" to the end of nums1
    2. a = float("-inf")
    
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            a = float("-inf") if i < 0 else nums1[i]
            b = float("-inf") if j < 0 else nums2[j]
            if a >= b:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
