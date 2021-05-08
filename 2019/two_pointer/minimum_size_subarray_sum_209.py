class Solution(object):
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n <= 0: return 0
        l = 0; h = 0; sum = 0;res = n+1
        while l<n:
            if sum < s and h < n:
                sum += nums[h]
                h += 1
            else:
                if sum >= s:
                    res = min(res, h-l)
                sum -= nums[l]
                l += 1
        return res if res < n+1 else 0

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
