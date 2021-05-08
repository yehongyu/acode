class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # write you code here
        nums = [3, 7]
        dp = [False] * (x+1)
        dp[0] = True
        for num in nums:
            for j in range(num, x+1):
                dp[j] = dp[j] | dp[j-num]
        if dp[x]:
            return 'YES'
        return 'NO'


s = Solution()
print(s.isBuild(10))
print(s.isBuild(5))
print(s.isBuild(13))
print(s.isBuild(14))
print(s.isBuild(17))
