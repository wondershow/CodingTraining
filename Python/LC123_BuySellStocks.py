class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxProfitUntil = [0] * N
        maxProfitSince = [0] * N
        minSeen = prices[0]
        for i in range(1, N):
            maxProfitUntil[i] = max(maxProfitUntil[i - 1], max(0, prices[i] - minSeen))
            minSeen = min(prices[i], minSeen)
        maxSeen = prices[-1]
        for i in range(N - 2, -1, -1):
            maxProfitSince[i] = max(maxProfitSince[i + 1], max(0, maxSeen - prices[i]))
            maxSeen = max(maxSeen, prices[i])
        res = 0
        for i in range(2, N - 1):
            res = max(res, maxProfitSince[i] + maxProfitUntil[i - 1])
        return max(res, max(maxProfitSince))
