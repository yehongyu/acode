class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        if n <=0: return True
        if n <=1: return bits[0] == 0
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            if bits[i-1] == 0:
                dp[i] = dp[i-1]
                if i-2 >= 0: dp[i] |= dp[i-2]
            elif bits[i-1] == 1:
                if i-2 >= 0 and bits[i-2] == 1:
                    dp[i] = dp[i-2]
        print(dp)
        return dp[n-1] and dp[n]

s = Solution()
bits = [1,1,1,0]
bits = [1,0,0]
print(s.isOneBitCharacter(bits))