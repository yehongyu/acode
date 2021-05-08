#coding=utf-8

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(2, n+1):
            cnt = 1
            for j in range(2, i+1):
                if i % j == 0:
                    cnt += 1
            if cnt % 2 == 1:
                res += 1
        return res




s = Solution()
print(s.bulbSwitch(3))
print(s.bulbSwitch(4))
print(s.bulbSwitch(5))
print(s.bulbSwitch(10))
