class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [-1] * (days[-1]+1)
        for day in days:
            dp[day] = 0
        dp[0] = 0
        for i in range(1, days[-1]+1):
            if dp[i] == -1: dp[i] = dp[i-1]
            else:
                cur = dp[i-1] + costs[0]
                cur = min(cur, dp[max(0,i-7)]+costs[1])
                cur = min(cur, dp[max(0,i-30)]+costs[2])
                dp[i] = cur
            print(i, dp[i])
        return dp[days[-1]]

s = Solution()
days = [1,4,6,7,8,20]; costs = [2,7,15]
print(s.mincostTickets(days, costs))
