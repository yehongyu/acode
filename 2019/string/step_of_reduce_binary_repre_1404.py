class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 0: return 0
        c = 0
        res = 0
        for i in range(n-1, -1, -1):
            val = int(s[i]) + c
            if i==0 and val < 2: break
            if val == 0:
                res += 1
                c = 0
            elif val == 1:
                res += 2
                c = 1
            elif val == 2:
                res += 1
                c = 1
        return res

s = Solution()
print(s.numSteps("1101"))
print(s.numSteps("10"))
print(s.numSteps("11"))

