class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def helper(self, nums, l, r, k):
        if l == r and k == 1:
            return nums[l]
        if l + 1 == r:
            return max(nums[l], nums[r]) if k == 1 else min(nums[l], nums[r])

        print(l, r, k)
        s = l+1
        e = r
        key = nums[l]
        while s < e:
            while s < e and nums[s] < key:
                s += 1
            while e > s and nums[e] >= key:
                e -= 1
            if s < e:
                self.swap(nums, s, e)
                print('swap', s, e, nums)
        if r - e + 1 == k:
            return nums[e]
        elif r - e + 1 > k:
            return self.helper(nums, e, r, k)
        else:
            return self.helper(nums, l, e-1, k-(r-e+1))

    def partition(self, nums, left, right):
        if left == right:
            return left
        key = nums[left]
        l = left + 1
        r = right
        while l <= r:
            while l<=right and nums[l] < key:
                l += 1
            while r >left and nums[r] >= key:
                r -= 1
            if l < r:
                self.swap(nums, l, r)
        self.swap(nums, r, left)
        return r


    def sortColors(self, nums, k):
        # write your code here
        n = len(nums)
        left = 0;
        right = n - 1
        if k < 1 or k > n:
            return -1
        k = n-k
        while True:
            pos = self.partition(nums, left, right)
            if pos == k:
                return nums[pos]
            if k < pos:
                right = pos -1
            else:
                left = pos + 1


s = Solution()
nums = [25, 8, 2, 3, 4, 9]
print(s.sortColors(nums,0))
