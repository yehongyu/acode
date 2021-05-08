from functools import cmp_to_key

def cmp(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        if n <= 1: return n
        pairs = sorted(pairs, key=cmp_to_key(cmp))
        print(pairs)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])
        return res

s = Solution()
pairs = [[2, 3], [1, 2], [3, 4]]
print(s.findLongestChain(pairs))
