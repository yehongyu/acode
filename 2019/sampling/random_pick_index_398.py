#coding=utf-8


class Solution_1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_map = {}
        for i in range(len(nums)):
            if nums[i] not in self.num_map:
                self.num_map[nums[i]] = [i]
            else:
                self.num_map[nums[i]].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.num_map:
            high = len(self.num_map[target])
            import numpy as np
            index = np.random.randint(0, high)
            return self.num_map[target][index]
        return None

class Solution22(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        cnt = 0
        for i in range(len(self.nums)):
            val = self.nums[i]
            if target != val:
                continue
            cnt += 1
            import numpy as np
            if np.random.randint(0, cnt) == 0:
                res = i
        return res

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        index = None
        n = len(self.nums)
        cnt = 0
        for i in range(n):
            if self.nums[i] != target: continue
            p = random.randint(0, cnt)
            if p == 0:
                index = i
            cnt += 1
        return index


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3, 3, 3]
obj = Solution(nums)
print(obj.pick(3))
print(obj.pick(1))
