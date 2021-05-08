import sys
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        n = len(pages)
        if n <= 0: return 0
        if n == 1: return pages[0]
        if n <= k:
            return max(pages)
        dp = []
        for i in range(n):
            dp.append([sys.maxsize] * k)
        for j in range(k):
            dp[0][j] = pages[0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + pages[i]
        for i in range(1, n):
            for j in range(1, k):
                dp[i][j] = dp[i][j-1]
                tmp = 0
                for t in range(i-1, -1, -1):
                    tmp += pages[t+1]
                    dp[i][j] = min(dp[i][j], max(dp[t][j-1], tmp))
        return dp[n-1][k-1]

s = Solution()
print(s.copyBooks([3,2,4], 2))
print(s.copyBooks([3,2,4], 3))

