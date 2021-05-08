class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def get_tail_one(self, i):
        cnt = 0
        while i % 2 == 1:
            cnt += 1
            i = i>>1
        return cnt

    def countBits_TIME(self, num):
        # write your code here
        res = [0] * (num + 1)
        for i in range(1, num+1):
            if i % 2 == 1:
                res[i] = res[i-1] + 1
            else:
                cnt = self.get_tail_one(i-1)
                res[i] = res[i-1] - cnt + 1
        return res

    def countBits(self, num):
        # write your code here
        res = [0] * (num + 1)
        for i in range(1, num+1):
            if i % 2 == 1:
                res[i] = res[i-1] + 1
            else:
                res[i] = res[i//2]
        return res

s = Solution()
print(s.countBits(5))
