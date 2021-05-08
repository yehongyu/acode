import sys
import math
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares_math(self, n):
        # write your code here
        if n < 0: return -1
        if n <= 1: return n
        while n % 4 == 0: n = n/4
        if n % 8 == 7: return 4
        a = 0
        while a * a <= n:
            b = int(math.sqrt(n - a * a))
            if a * a + b * b == n:
                return 1 if a == 0 or b == 0 else 2
            a += 1
        return 3

    def numSquares_DP(self, n):
        # write your code here
        if n < 0: return -1
        if n <= 1: return n
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0
        for i in range(n+1):
            j = 1
            while i + j * j <= n:
                cur = i + j*j
                dp[cur] = min(dp[cur], dp[i] + 1)
                j += 1
        return dp[n]

    def numSquares(self, n):
        # write your code here
        if n < 0: return -1
        if n <= 1: return n
        dp = [0]
        while len(dp) <= n:
            m = len(dp)
            cur = sys.maxsize
            i = 1
            while i * i <= m:
                cur = min(cur, dp[m-i*i]+1)
                i += 1
            dp.append(cur)
        return dp[-1]

s = Solution()
print(s.numSquares(13))
