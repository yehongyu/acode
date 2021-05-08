class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            cur = nums[i]
            if target -cur in map:
                return [map[target-cur], i]
            map[cur] = i
    
