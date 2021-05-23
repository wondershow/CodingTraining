class Solution:
    
    """
    DP[i] means the min cost to cover all travel days until day i of a year.
    We need to create an array of size 366. We can not use a dp array of size len(days)
    because days[i] - 7 might not be in days. So we can not control 
    
    """
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        all_days = set(days)
        dp = [float(inf)] * 366
        dp[0] = 0
        
        for day in range(1, 366):
            if day not in all_days:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min([dp[day - 1] + costs[0], dp[max(0, day - 7)] + costs[1], dp[max(0, day - 30)] + costs[2]])
        return dp[days[-1]]
                
