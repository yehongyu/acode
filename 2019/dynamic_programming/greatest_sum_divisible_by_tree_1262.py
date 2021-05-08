class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0
        dp1 = [None] * 3
        dp2 = [None] * 3
        for i in range(n):
            d = nums[i] / 3
            r = nums[i] % 3
            for j in range(3):
                if dp1[j] != None:
                    tmp_d = (j + r) / 3
                    tmp_r = (j + r) % 3
                    if dp1[tmp_r] == None:
                        dp2[tmp_r] = dp1[j] + d + tmp_d
                    else:
                        dp2[tmp_r] = max(dp1[tmp_r], dp1[j] + d + tmp_d)
                    print('i-j', i, j, dp2)
            if dp2[r] == None:
                dp2[r] = d
            else:
                dp2[r] = max(dp2[r], d)
            print(i, dp2)
            dp1 = dp2[0:]
        return dp1[0] * 3 if dp1[0] != None else 0

s = Solution()
nums = [3,6,5,1,8]
nums = [1,2,3,4,4]
nums = [4]
print(s.maxSumDivThree(nums))

