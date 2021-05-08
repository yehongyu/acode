class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        n = len(numbers)
        if n <= 1:
            return None
        nums = []
        for i in range(n):
            nums.append((numbers[i], i))
        nums = sorted(nums, key=lambda x:x[0])
        left = 0
        right = n-1
        while left < right:
            cur = nums[left][0] + nums[right][0]
            if cur == target:
                return [min(nums[left][1], nums[right][1]),
                        max(nums[left][1], nums[right][1])]
            elif cur > target:
                right -= 1
            else:
                left += 1
        return None

    def twoSum_map(self, numbers, target):
        n = len(numbers)
        if n <= 1:
            return None
        n_map = {}
        for i in range(n):
            if numbers[i] not in n_map:
                n_map[numbers[i]] = [i]
            else:
                n_map[numbers[i]].append(i)
        for i in range(n):
            a = numbers[i]
            b = target-numbers[i]
            if b not in n_map: continue
            elif a != b:
                return [min(i, n_map[b][0]), max(i, n_map[b][0])]
            else:
                if len(n_map[a]) >= 2:
                    return n_map[a][0:2]
        return None


    def threeSum(self, numbers):
        n = len(numbers)
        if n <= 2:
            return []
        nums = []
        for i in range(n):
            nums.append((numbers[i], i))
        nums = sorted(nums, key=lambda x: x[0])
        res = []
        for i in range(n-2):
            left = i+1
            right = n - 1
            cur = - nums[i][0]
            if i > 0 and nums[i][0] == nums[i-1][0]: continue
            while left < right:
                tmp = nums[left][0] + nums[right][0]
                if tmp == cur:
                    res.append(
                        [nums[i][0], nums[left][0], nums[right][0]])
                    left += 1
                    while left < right and nums[left][0] == nums[left-1][0]:
                        left += 1
                elif tmp > cur:
                    right -= 1
                else:
                    left += 1
        return res

    def fourSum(self, numbers, target):
        n = len(numbers)
        n_map = {}
        for i in range(n-1):
            for j in range(i, n):
                sum = numbers[i] + numbers[j]
                if sum not in n_map:
                    n_map[sum] = [[i, j]]
                else:
                    n_map[sum].append([i, j])
        res = []
        for sum in n_map.keys():
            cur = target - sum
            if cur not in n_map: continue
            elif sum == cur and len(n_map[sum]) > 1:
                for i in range(len(n_map[sum])-1):
                    for j in range(i, len(n_map[sum])):
                        ai, bi = n_map[sum][i]
                        ci, di = n_map[sum][i]
                        if ai != ci and ai != di and bi != ci and bi != di:
                            res.append([numbers[ai], numbers[bi],
                                        numbers[ci], numbers[di]])
        return 0

    def kSum(self, A, k, target):
        n = len(A)
        if k > n:
            return 0
        dp = []
        for i in range(n+1):
            tmp = []
            for j in range(k+1):
                tmp.append([0] * (target+1))
            dp.append(tmp)
            dp[i][0][0] = 1
        dp[0][0][0] = 1
        print(0, 0, dp[0][0])
        print(0, 1, dp[0][1])
        print(1, 0, dp[1][0])
        for i in range(1, n+1):
            for j in range(1, k+1):
                for t in range(1, target+1):
                    if t-A[i-1] >= 0:
                        print(i-1, j-1, t-A[i-1])
                        dp[i][j][t] = dp[i-1][j-1][t-A[i-1]] + dp[i-1][j][t]
                    else:
                        dp[i][j][t] = dp[i-1][j][t]
                print(i, j, dp[i][j])
        return dp[n][k][target]




s = Solution()
print(s.kSum([1,2,3,4], 2, 5))

'''
print(s.twoSum_map([2, 7, 11, 15], 9))
print(s.twoSum_map([15, 2, 7, 11], 9))
print(s.twoSum_map([0, 4, 3, 0], 0))

print(s.threeSum([2, 7, 11, 15]))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([1,0,-1,-1,-1,-1,0,1,1,1]))
'''
