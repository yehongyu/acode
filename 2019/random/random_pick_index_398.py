class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        import random
        res = None
        n = len(self.nums)
        cnt = 0
        for i in range(n):
            if self.nums[i] != target: continue
            pro = random.randint(0, cnt)
            if pro == 0:
                res = i
            cnt += 1
        return res



s = Solution([1,2,3,1,3,2,3])

map = {}
for i in range(10000):
    idx = s.pick(3)
    if idx not in map: map[idx] = 0
    map[idx] += 1
print(map)
