class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 2:
            return n
        p1 = 1; p2 = 1; p3 = 2;
        res = 0
        for i in range(3, n):
            res = p1 + p2 + p3
            p1 = p2
            p2 = p3
            p3 = res
        return res

s = Solution()
print(s.climbStairs2(3))
print(s.climbStairs2(4))
print(s.climbStairs2(5))
print(s.climbStairs2(6))

