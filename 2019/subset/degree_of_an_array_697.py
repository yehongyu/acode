class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        n_map = {}
        max_cnt = 0
        for i in range(n):
            if nums[i] not in n_map:
                n_map[nums[i]] = []
            n_map[nums[i]].append(i)
            max_cnt = max(len(n_map[nums[i]]), max_cnt)
        min_len = n
        print(n_map)
        for val in n_map.keys():
            if len(n_map[val]) == max_cnt:
                min_len = min(min_len, n_map[val][-1] - n_map[val][0] + 1)
        return min_len

s = Solution()
nums = [1,2,2,3,1,4,2]
nums = [1,2,2,3,1]
print(s.findShortestSubArray(nums))
