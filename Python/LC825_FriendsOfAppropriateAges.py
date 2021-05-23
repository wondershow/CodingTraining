class Solution:
    """
        1. Use buckets
        2. When age1 == age2 it is f(age1) * [f(age1) - 1]
    """
    def numFriendRequests(self, ages: List[int]) -> int:
        age_bucket = [0] * 121
        for age in ages:
            age_bucket[age] += 1
        res = 0
        for a in range(1, 121):
            for b in range(1, a + 1):
                if b <= a // 2 + 7:
                    continue
                if b > 100 and a < 100:
                    continue
                if b == a:
                    res += age_bucket[a] * (age_bucket[a] - 1)
                else:
                    res += age_bucket[a] * age_bucket[b]
        return res
