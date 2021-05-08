class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        if num < 0 : return res
        res = [0] * (num + 1)
        res[1] = 1
        for i in range(2, num+1):
            if i % 2 == 0:
                res[i] = res[i>>1]
            else:
                res[i] = res[i>>1] + 1
        return res

s = Solution()
print(s.countBits(5))
