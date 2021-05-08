class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if k <=0 or n < k: return []
        vec = []
        res = []
        for i in range(n):
            if len(vec) > 0 and i-vec[0] >= k:
                vec.pop(0)
            while len(vec)>0 and nums[vec[-1]] <= nums[i]:
                vec.pop(-1)
            vec.append(i)
            if i >= k-1:
                res.append(nums[vec[0]])
        return res

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]; k = 3
print(s.maxSlidingWindow(nums, k))
