import random
class Solution:
    def select(self, n, k):
        res = []
        for i in range(1, n+1):
            if i <= k:
                res.append(i)
                continue
            prob = random.randint(1, i-1)
            print('prob:', i, prob)
            if prob < i:
                idx = random.randint(0, k-1)
                res[idx] = i
                print('idx:', i, prob, idx, res)
        return res

    def sample(self, nums, k):
        n = len(nums)
        reservoir = []
        for i in range(0, n):
            if i < k:
                reservoir.append(nums[i])
                continue
            p = random.randint(0, i)
            if p < k:
                reservoir[p] = nums[i]
        return reservoir

    def swap(self, nums, i, j):
        if i == j: return
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def shuffle(self, nums):
        n = len(nums)
        res = nums[0:]
        for i in range(n):
            p = random.randint(0, i)
            if p < i:
                self.swap(res, p, i)
        return res

    def choice(self, nums):
        n = len(nums)
        res = None
        for i in range(n):
            p = random.randint(0, i)
            if p == 0:
                res = nums[i]
        return res

    def choice_weight(self, nums, weight):
        n = len(nums)
        res = None; cnt = 0
        for i in range(n):
            for j in range(weight[i]):
                p = random.randint(0, cnt)
                if p == 0:
                    res = nums[i]
                cnt += 1
        return res


s = Solution()
#print(s.sample(10, 3))

nums = [40, 2, 13, 9, 8, 6, 5, 3]
map = {}
for num in nums:
    map[num] = 0

for i in range(10000):
    res = s.shuffle(nums)
    map[res[0]] += 1
print(map)

nums = [40, 2, 13, 9, 8, 6, 5, 3]
map = {}
for num in nums:
    map[num] = 0
for i in range(10000):
    res = s.sample(nums, 3)
    for val in res:
        map[val] += 1
print(map)

nums = [40, 2, 13, 9, 8, 6, 5, 3]
map = {}
for num in nums:
    map[num] = 0
for i in range(10000):
    val = s.choice(nums)
    map[val] += 1
print(map)

nums = [40, 2, 13, 9, 8, 6, 5, 3]
weight = [1, 1, 2, 1, 3, 1, 1, 1]
map = {}
for num in nums:
    map[num] = 0
for i in range(10000):
    val = s.choice_weight(nums, weight)
    map[val] += 1
print(map)
