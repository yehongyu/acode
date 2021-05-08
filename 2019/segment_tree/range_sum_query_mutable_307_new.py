#coding=utf-8
import math

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums[0:]
        self.size = int(math.sqrt(len(nums)))
        self.block = [0] * int(math.ceil(len(nums)/float(self.size)))
        for i in range(0, len(nums)):
            self.block[i/self.size] += nums[i]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        delta = val - self.data[i]
        self.block[i/self.size] += delta
        self.data[i] = val


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        start = i / self.size
        end = j / self.size
        if start == end:
            return sum(self.data[i:j+1])
        res = 0
        b1 = start * self.size + self.size
        res += sum(self.data[i:b1])
        if start + 1 < end:
            res += sum(self.block[start+1:end])
        res += sum(self.data[end*self.size:j+1])
        return res


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0,2))
obj.update(1,2)
print(obj.sumRange(0,2))
