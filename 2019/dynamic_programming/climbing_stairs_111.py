class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 0:
            return 0
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n+1)
        dp_2 = 1;
        dp_1 = 2;
        res = 0
        for i in range(3, n+1):
            res = dp_1 + dp_2
            dp_2 = dp_1
            dp_1 = res
        return res
