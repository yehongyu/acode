class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    def findpos(self, nums, l, h):
        start = l
        val = nums[l]
        while l < h:
            while l < h and nums[h] > val: h -= 1
            while l < h and nums[l] <= val: l += 1
            if l < h:
                self.swap(nums, l, h)
        self.swap(nums, start, h)
        return h

    def median(self, nums):
        # write your code here
        n = len(nums)
        if n == 0: return None
        if n == 1: return nums[0]
        mid = (n-1)//2
        left = 0; right = n -1
        print(mid)
        while left < right:
            pos = self.findpos(nums, left, right)
            print(pos, nums[pos])
            if pos > mid:
                right = pos - 1
            elif pos < mid:
                left = pos + 1
            else:
                return mid
        return right

    def wiggleSort(self, nums):
        n = len(nums)
        if n <= 1: return
        mid = self.median(nums)
        if mid % 2 == 0:
            h = mid + 2
        else:
            h = mid + 1
        l = 1;
        print(nums)
        while l < mid and h < n:
            print(l, h)
            self.swap(nums, l, h)
            l += 2; h += 2



s = Solution()
nums = [4, 5, 1, 2, 3]
nums = [1,3,2,2,3,1]
#print(s.median(nums))
s.wiggleSort(nums)
print(nums)


