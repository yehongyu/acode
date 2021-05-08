#coding=utf-8

class Solution1(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        sum = [0] * (size + 1)
        for i in range(size):
            sum[i+1] = sum[i] +nums[i]
        res = 0
        for i in range(size):
            for j in range(i, size):
                if lower <= sum[j+1]-sum[i] <= upper:
                    res += 1
        return res

class Solution(object):
    def mergeSort(self, sum, lower, upper, left, right):
        if right - left <= 1: return 0
        mid = left + (right-left)/2
        count = self.mergeSort(sum, lower, upper, left, mid) + \
            self.mergeSort(sum, lower, upper, mid, right)

        m = mid; n = mid;
        for i in range(left, mid):
            while m < right and sum[m] - sum[i] < lower:
                m += 1
            while n < right and sum[n] - sum[i] <= upper:
                n += 1
            count += n - m
        return count


    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        size = len(nums)
        sum = [0] * (size+1)
        for i in range(size):
            sum[i+1] = sum[i] + nums[i]
        return self.mergeSort(sum, lower, upper, 0, size+1)



s = Solution()
nums = [-2, 5, -1]
lower = -2
upper = 2
print(s.countRangeSum(nums, lower, upper))
