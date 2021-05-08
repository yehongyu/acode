class Solution(object):
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def partion(self, nums, l, h):
        if l == h: return l
        cur = l
        val = nums[l]
        while l < h:
            while l < h and nums[h] > val: h -= 1
            while l < h and nums[l] <= val: l += 1
            if l < h: self.swap(nums, l, h)
        self.swap(nums, cur, h)
        return h

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < k: return None
        key = n-k
        l = 0; h = n-1
        while l <= h:
            pos = self.partion(nums, l, h)
            if pos == key: return nums[pos]
            elif pos < key:
                l = pos + 1
            else:
                h = pos - 1

s = Solution()
nums = [3,2,1,5,6,4]; k = 7
print(s.findKthLargest(nums, k))