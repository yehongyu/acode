class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0: return 0
        if dividend == divisor: return 1
        m = abs(dividend)
        n = abs(divisor)
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        res = 0
        while m >= n:
            shift = 0
            while m >= (n << shift):
                shift += 1
            m -= n << (shift - 1)
            res += 1 << (shift - 1)
        if sign == -1:
            return 0 - res
        return res

s = Solution()
print(s.divide(1, -1))

