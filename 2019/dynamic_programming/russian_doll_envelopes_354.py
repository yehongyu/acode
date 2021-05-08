from functools import cmp_to_key
def cmp(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n <= 1: return n
        envelopes = sorted(envelopes, key=cmp_to_key(cmp))
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res

s = Solution()
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(s.maxEnvelopes(envelopes))
