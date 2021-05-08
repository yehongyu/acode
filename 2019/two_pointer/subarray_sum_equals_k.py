class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n <= 0: return 0
        acc_map = {}; sum = 0
        acc_map[0] = 1
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in acc_map:
                res += acc_map[sum-k]
            if sum not in acc_map:
                acc_map[sum] = 0
            acc_map[sum] += 1
        return res

    def numSubarraysWithSum(self, nums, k):
        n = len(nums)
        if n <= 0: return 0
        acc_map = {}; sum = 0
        acc_map[0] = 1
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in acc_map:
                res += acc_map[sum-k]
            if sum not in acc_map:
                acc_map[sum] = 0
            acc_map[sum] += 1
        return res


    def checkSubarraySum(self, nums, k):
        n = len(nums)
        if n < 2: return False
        acc_map = {}; sum = 0
        acc_map[0] = -1
        if k == 0:
            for i in range(1, n):
                if nums[i-1] == 0 and nums[i] == 0:
                    return True
            return False

        for i in range(n):
            sum = (sum + nums[i]) % k
            print(i, sum, acc_map)
            if sum in acc_map and i - acc_map[sum] >= 2:
                return True
            if sum not in acc_map:
                acc_map[sum] = i
        return False

    def subarraysDivByK(self, A, K):
        n = len(A)
        if n <= 0: return 0
        if K == 0: return 0
        acc_map = {}; acc_map[0] = 1
        res = 0; sum = 0
        for i in range(n):
            sum = (sum + A[i]) % K
            if sum in acc_map:
                res += acc_map[sum]
                acc_map[sum] += 1
            else:
                acc_map[sum] = 1
        return res

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def maximumSwap(self, num):
        if num < 10: return num
        nums = []
        while num > 0:
            cur = num % 10
            nums.insert(0, cur)
            num = num // 10
        back = [0] * len(nums)
        back[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            back[i] = max(nums[i], back[i+1])
        flag = False
        for i in range(len(nums)):
            if flag: continue
            if nums[i] == back[i]: continue
            for j in range(len(nums)-1, i, -1):
                if nums[j] == back[i]:
                    self.swap(nums, i, j)
                    flag = True
                    break
        res = 0
        for val in nums:
            res = res * 10 + val
        return res

    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        if n < k: return 0
        cnt_map = {}
        cnt_map[0] = 1; cnt = 0; res = 0
        for num in nums:
            if num % 2 == 1:
                cnt += 1
            idx = cnt - k
            if idx in cnt_map:
                res += cnt_map[idx]
            if cnt not in cnt_map:
                cnt_map[cnt] = 0
            cnt_map[cnt] += 1
        return res




s = Solution()
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(s.numberOfSubarrays(nums, k))
#print(s.maximumSwap(2736))
#print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
#print(s.checkSubarraySum([23, 2, 2, 6, 7], 6))
#print(s.checkSubarraySum([1, 0, 1, 0, 1], 4))

#print(s.subarraySum([1,1,1], 2))
