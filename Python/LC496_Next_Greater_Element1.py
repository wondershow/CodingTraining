class Solution(object):
    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack, map_next_element = [], {}
        for num in nums2:
            while stack and num > stack[-1]:
                map_next_element[stack.pop()] = num
            stack.append(num)
        while stack:
            map_next_element[stack.pop()] = -1
        
        return [map_next_element[a] for a in nums1]

    def nextGreaterElement(self, nums1, nums2):
        stack, map_next_element, N = [], {}, len(nums2)
        for i in range(N - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                map_next_element[nums2[i]] = stack[-1]
            else:
                map_next_element[nums2[i]] = -1
            stack.append(nums2[i])
        return [map_next_element[num] for num in nums1]


