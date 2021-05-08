class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n == 1:
            return k
        pre_same = 0
        pre_diff = k
        for i in range(1, n):
            cur_diff = (k-1) * (pre_same + pre_diff)
            cur_same = pre_diff
            pre_diff = cur_diff
            pre_same = cur_same
        return pre_diff + pre_same


s = Solution()
print(s.numWays(3, 2))
