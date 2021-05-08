class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings_I(self, s):
        # write your code here
        n = len(s)
        if n <= 0: return 0
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 1 if int(s[n-1]) > 0 else 0
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                if int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
                dp[i] += dp[i+1]
            print(i, dp[i], dp)
        return dp[0]

    def numDecodings(self, s):
        n = len(s)
        if n <= 0: return 0
        dp = [0] * (n+1)
        dp[n] = 1
        if s[n-1] == '*':
            dp[n-1] = 9
        elif s[n-1] == '0':
            dp[n-1] = 0
        else:
            dp[n-1] = 1
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            elif s[i] == '*':
                dp[i] = 9 * dp[i+1]
                if s[i+1] == '*':
                    dp[i] += 15 * dp[i+2]
                elif int(s[i+1]) <= 6:
                    dp[i] += 2 * dp[i+2]
                else:
                    dp[i] += dp[i+2]
            else:
                print(dp[i+1], dp)
                dp[i] += dp[i+1]
                if s[i+1] == '*':
                    if s[i] == '1': dp[i] += 9 * dp[i+2]
                    if s[i] == '2': dp[i] += 6 * dp[i+2]
                elif int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
            print(i, dp[i], dp)
        return dp[0]


s = Solution()
#print(s.numDecodings('19261001'))
print(s.numDecodings('1*'))
print(s.numDecodings('2*'))
print(s.numDecodings('**1**'))

