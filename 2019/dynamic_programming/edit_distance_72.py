class Solution(object):
    def minDistance_3op(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0: return n
        if n == 0: return m
        if word1 == word2: return 0
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        dp[0][0] = 0
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        return dp[m][n]

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0: return n
        if n == 0: return m
        if word1 == word2: return 0
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        dp[0][0] = 0
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1
        return dp[m][n]


    def minimumDeleteSum(self, word1, word2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m == 0: return n
        if n == 0: return m
        if word1 == word2: return 0
        dp = []
        for i in range(m+1):
            dp.append([0] * (n+1))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(word1[i-1])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        res = 0
        for i in range(m):
            res += ord(word1[i])
        for i in range(n):
            res += ord(word2[i])
        return res - 2 * dp[m][n]



s = Solution()
word1 = "sea";
word2 = "eat"
#print(s.minDistance(word1, word2))
print(s.minimumDeleteSum(word1, word2))


'''
word1 = "horse"; word2 = "ros"
word1 = "intention"; word2 = "execution"
print(s.minDistance(word1, word2))
'''
