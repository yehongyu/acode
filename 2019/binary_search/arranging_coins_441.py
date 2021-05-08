class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        if n == 1: return 1
        l = 1; h = n
        t = 2 * n
        while l < h:
            mid = l + (h-l)//2
            cur = mid * (mid+1)
            if cur == t:
                return mid
            elif cur > t:
                h = mid
            else:
                l = mid + 1
        return h-1

s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(16))
