class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        print(x, n)
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1/x
        k = n
        if n < 0:
            k = n+1
        tmp = self.myPow(x, k//2)
        if n % 2 == 0:
            return tmp * tmp
        else:
            if n > 0:
                return x * tmp * tmp
            else:
                return tmp * tmp / x

    def sqrt(self, x):
        if x < 0: return None
        if x == 1: return x
        start = 1; end = x
        while start + 1 < end:
            mid = start + (end-start)//2
            print(start, mid, end)
            if mid > x // mid:
                end = mid
            elif mid == x // mid:
                return mid
            else:
                start = mid
        return mid

s = Solution()
#print(s.myPow(0.44894, -5))
print(s.sqrt(4187))
