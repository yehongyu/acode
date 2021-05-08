class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(32):
            tmp = 0
            for num in nums:
                tmp += (num >> i) & 1
            print(i, tmp)
            res |= (tmp % 3) << i
        return res

s = Solution()
nums =[2,2,3,2]
nums =[1,0,1,0,99,1,0]
nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
print(s.singleNumber(nums))
