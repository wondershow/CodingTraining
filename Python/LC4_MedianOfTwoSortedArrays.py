class Solution:
    """
    Mistakes made:
    Failed to consider the case when num2 is empty
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth_smallest(nums1, nums2, k):
            if len(nums1) < len(nums2):
                return kth_smallest(nums2, nums1, k)
            
            # Missed this part
            if not nums2:
                return nums1[k - 1]
            if k == 1:
                return min(nums1[0], nums2[0])
            
            half_k = k // 2
            right_half = min(half_k, len(nums2))
            if nums1[half_k - 1] < nums2[right_half - 1]:
                return kth_smallest(nums1[half_k:], nums2, k - half_k)
            return kth_smallest(nums1, nums2[right_half:], k - right_half)
        
        return (kth_smallest(nums1, nums2, 1 + (len(nums1) + len(nums2) - 1) // 2) + kth_smallest(nums1, nums2, 1 + (len(nums1) + len(nums2)) // 2)) / 2
