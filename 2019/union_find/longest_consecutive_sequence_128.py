#coding=utf-8

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        done_set = set()
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            if num in done_set:
                continue
            start = num - 1
            while start in nums:
                done_set.add(start)
                start -= 1
            end = num + 1
            while end in nums:
                done_set.add(end)
                end += 1
            cnt = end - start - 1
            res = max(res, cnt)
        return res

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
