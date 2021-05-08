class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = [0] * 32
        for i in range(32):
            for num in nums:
                vals[i] += (num >> i) & 1
                vals[i] = vals[i] % 3
        res = 0
        for i in range(32):
            res += vals[i] << i
        return res

s = Solution()
print(s.singleNumber([2,2,3,2]))
print(s.singleNumber([0,1,0,1,0,1,99]))
