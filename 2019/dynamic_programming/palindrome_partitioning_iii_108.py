import sys
class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def getPalind(self, s):
        n = len(s)
        isPalind = []
        for i in range(n):
            isPalind.append([False] * n)
        for i in range(n):
            isPalind[i][i] = True
        for step in range(1, n):
            for i in range(n-step):
                if step == 1:
                    isPalind[i][i+step] = s[i] == s[i+step]
                else:
                    isPalind[i][i+step] = s[i] == s[i+step] and isPalind[i+1][i+step-1]
        return isPalind

    def minCut(self, s):
        # write your code here
        n = len(s)
        if n <= 1:
            return 0
        isPalind = self.getPalind(s)
        dp = [n] * (n+1)
        dp[0] = -1
        dp[1] = 0
        for i in range(2, n+1):
            for j in range(0, i):
                if isPalind[j][i-1]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n]


s = Solution()
print(s.minCut("bcbabac"))
