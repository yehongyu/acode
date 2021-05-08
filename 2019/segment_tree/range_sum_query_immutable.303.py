#coding=utf-8

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = [0]
        for i in range(len(nums)):
            self.sums.append(self.sums[i]+nums[i])


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1]-self.sums[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    na = NumArray(nums)
    print na.sumRange(0, 2)
    print na.sumRange(2, 5)
    print na.sumRange(0, 5)
