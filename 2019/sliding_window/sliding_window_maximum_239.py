#coding=utf-8

class Solution(object):
    def maxSlidingWindow_fore_rute(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        size = len(nums)
        res = []
        if size <= 1:
            return nums
        for i in range(size-k+1):
            tmp = nums[i]
            for j in range(i+1, i+k):
                tmp = max(tmp, nums[j])
            res.append(tmp)
        return res

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        vec = []
        res = []
        for i in range(len(nums)):
            if len(vec) > 0 and i - vec[0] >= k:
                vec = vec[1:]
            while len(vec) > 0 and nums[i] >= nums[vec[-1]]:
                vec = vec[0:len(vec)-1]
            vec.append(i)
            if i >= k-1:
                res.append(nums[vec[0]])
            print(i, vec, res)
        return res



s = Solution()
#print(s.maxSlidingWindow([], 0))
#print(s.maxSlidingWindow([1], 1))
#print(s.maxSlidingWindow([1, 2, 3], 2))
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
