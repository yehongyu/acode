import random
class Solution:
    # equal possibility

    # reservoir sampling
    def select(self, n, k):
        res = []
        if n < k or k <= 0: return res
        if n == k: return [i for i in range(n)]
        for i in range(n):
            if len(res) < k:
                res.append(i)
                continue
            rnd = random.randint(0, i)
            if rnd <= k-1:
                res[rnd] = i
        return res

    def sample(self, nums, k):
        size = len(nums)
        if k <= 0: return []
        if size <= k: return nums
        res = []
        for i in range(size):
            v = nums[i]
            if len(res) < k:
                res.append(v)
                continue
            rnd = random.randint(0, i)
            if rnd < k:
                res[rnd] = v
        return res

    def shuffle(self, nums):
        size = len(nums)
        for i in range(1, size):
            v = nums[i]
            rnd = random.randint(0, i)
            if rnd != i:
                nums[i], nums[rnd] = nums[rnd], nums[i]
        return nums

    # choice === sample(k=1)
    def choice(self, nums):
        size = len(nums)
        if size < 1: return None
        res = None
        for i in range(size):
            v = nums[i]
            rnd = random.randint(0, i)
            if rnd == 0:
                res = v
        return res


    def choice_weight(self, nums, weight):
        res = None
        size = len(nums)
        cnt = 0
        for i in range(size):
            v = nums[i]
            for j in range(weight[i]):
                rnd = random.randint(0, cnt)
                if rnd == 0:
                    res = v
                cnt += 1
        return res

    def choice_float_weight(self, nums, weight):
        size = len(nums)
        if size <= 0: return None
        total_weight = float(sum(weight))
        acc_weight = [0]
        for i in range(size):
            tmp = acc_weight[i] + weight[i]/total_weight
            acc_weight.append(tmp)
        res = None
        for i in range(size):
            rnd = random.random() * acc_weight[i+1]
            if acc_weight[i] <= rnd:
                res = nums[i]
        return res



if __name__ == "__main__":
    s = Solution()
    cnt = 10000
    from collections import defaultdict
    cnt_map = defaultdict(int)
    #cnt_map = defaultdict(dict)
    nums = [i for i in range(5)]
    weights = [1.3, 5.3, 6.6, 8.9, 9.1]
    total_weight = sum(weights)
    acc_weight = [0]
    for i in range(len(nums)):
        tmp = weights[i]/total_weight
        acc_weight.append(tmp)
    print(acc_weight)
    for i in range(cnt):
        #res = s.select(10, 5)
        '''
        nums = [10,8,4,-2,-10,-5, 88, 99999, 22222]
        res = s.sample(nums, 5)
        for v in res:
            cnt_map[v] += 1
        '''
        '''
        nums = [i for i in range(3)]
        res = s.shuffle(nums)
        for i in range(len(nums)):
            if res[i] not in cnt_map[i]:
                cnt_map[i][res[i]] = 0
            cnt_map[i][res[i]] += 1
        '''
        #res = s.choice(nums)
        #res = s.choice_weight(nums, weights)
        res = s.choice_float_weight(nums, weights)
        cnt_map[res] += 1
    for v in sorted(cnt_map.keys()):
        print(v, ":", cnt_map[v])