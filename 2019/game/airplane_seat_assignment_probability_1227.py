#coding=utf-8

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n < 1: return 0
        if n == 1: return 1.0
        dp = [0] * n
        sum = 0
        for i in range(1, n):
            dp[i] = (1+sum) / float(i+1)
            sum += dp[i]
        return dp[n-1]

s = Solution()
#print(s.nthPersonGetsNthSeat(0))
#print(s.nthPersonGetsNthSeat(1))
print(s.nthPersonGetsNthSeat(2))
print(s.nthPersonGetsNthSeat(3))
print(s.nthPersonGetsNthSeat(4))
print(s.nthPersonGetsNthSeat(10000))
