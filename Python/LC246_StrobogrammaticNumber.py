class Solution:
    """
    Mistakes made, 
    used 's' instead 'num'
    did not consider the case when num[l] not a key in map
    """
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {"1":"1", "0" : "0", "8":"8", "6":"9", "9":"6"}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in mirror or mirror[num[l]] != num[r]:
                return False
            l, r = l + 1, r - 1
        return True
