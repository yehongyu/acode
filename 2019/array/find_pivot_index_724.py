class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3: return False
        acc = [0]
        for i in range(n):
            acc.append(acc[-1] + nums[i])
        for i in range(1, n-1):
            if acc[i] == acc[n] - acc[i+1]:
                return i
        return -1

s = Solution()

nums = [1, 7, 3, 6, 5, 6]
print(s.pivotIndex(nums))