class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        res, i = 0, 1
        while i < len(arr) - 1:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left, right = i - 1, i + 1
                while left >= 0 and arr[left] < arr[left + 1]:
                    left -= 1
                while right < len(arr) and arr[right - 1] > arr[right]:
                    right += 1
                res = max(res, right - left - 1)
                i = right
            else:
                i += 1
        return res
