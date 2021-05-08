#coding=utf-8
import math

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums[0:]
        root = math.sqrt(len(nums))
        if root == 0:
            return
        self.len = int(math.ceil(len(nums) / root))
        self.block = [0] * self.len
        for i in range(0, len(nums)):
            self.block[i/self.len] += self.data[i]


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        dela = val - self.data[i]
        self.block[i/self.len] += dela
        self.data[i] = val


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        start = i / self.len
        end = j / self.len
        res = 0
        if start == end:
            for idx in range(i, j+1):
                res += self.data[idx]
            return res
        for idx in range(i, (start+1)*self.len):
            res += self.data[idx]
        for bidx in range(start+1, end):
            res += self.block[bidx]
        for idx in range(end*self.len, j+1):
            res += self.data[idx]
        return res

if __name__ == '__main__':
    nums = [1, 3, 5]
    na = NumArray(nums)
    print(na.sumRange(0, 2))
    print(na.update(1, 2))
    print(na.sumRange(0, 2))
