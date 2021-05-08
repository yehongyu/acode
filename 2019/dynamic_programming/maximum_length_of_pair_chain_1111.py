from functools import cmp_to_key
def cmp(x, y):
    if x[0] < y[0]:
        return -1
    if x[0] > y[0]:
        return 1
    if x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    else:
        return 0
class Solution:
    """
    @param pairs: pairs of numbers
    @return: the length longest chain which can be formed
    """
    def findLongestChain(self, pairs):
        # Write your code here
        n = len(pairs)
        if n <= 1: return n
        pairs = sorted(pairs, key=cmp_to_key(cmp))
        print(pairs)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        return dp[n-1]


s = Solution()
print(s.findLongestChain([[3,8], [1,2], [3,6]]))
