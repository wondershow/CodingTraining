  class Solution:
      def maxScore(self, cardPoints: List[int], k: int) -> int:
          N = len(cardPoints)
          k = N - k
          total = min_sum = sum(cardPoints[:k])
          for i in range(k, N):
              total -= cardPoints[i - k]
              total += cardPoints[i]
              min_sum = min(min_sum, total)
          return sum(cardPoints) - min_sum
