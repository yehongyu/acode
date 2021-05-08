class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 3: return []
        nums = sorted(nums)
        res = []
        for i in range(n):
            l = i+1; h= n-1
            if i-1 >= 0 and nums[i] == nums[i-1]: continue
            while l < h:
                cur = nums[l] + nums[h]
                if cur > -nums[i]:
                    while h-1 > l and nums[h] == nums[h-1]:
                        h -= 1
                    h -= 1
                elif cur < -nums[i]:
                    while l+1 < h and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[h]])
                    while h-1 > l and nums[h] == nums[h-1]:
                        h -= 1
                    h -= 1
        return res

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3: return []
        import sys
        diff = sys.maxsize; res = None
        nums = sorted(nums)
        for i in range(n):
            l = i+1; h=n-1
            while l < h:
                cur = nums[i] + nums[l] + nums[h]
                cur_diff = abs(cur-target)
                if cur_diff < diff:
                    res = cur; diff = cur_diff
                if cur > target:
                    h -= 1
                elif cur < target:
                    l += 1
                else:
                    return target
        return res





s = Solution()

#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.threeSum([0, 0, 0, 0]))

#print(s.threeSumClosest([-1, 2, 1, -4], 1))
print(s.threeSumClosest([1, 1, 1, 0], -100))
