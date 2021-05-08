class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        n = len(nums)
        if n <= 0:
            return -1
        res = nums[0]
        cur = nums[0]
        for i in range(1, n):
            if cur > 0:
                cur = nums[i] + cur
            else:
                cur = nums[i]
            res = max(cur, res)
        return res


    def minimumSubarray(self, nums):
        n = len(nums)
        if n <= 0:
            return -1
        res = nums[0]
        cur = nums[0]
        for i in range(1, n):
            if cur < 0:
                cur = nums[i] + cur
            else:
                cur = nums[i]
            res = min(cur, res)
        return res

    def maxDiffSubArrays_too_long(self, nums):
        n = len(nums)
        if n <= 1:
            return -1
        if n == 2:
            return abs(nums[1] - nums[0])

        cur = nums[0]
        max_res = nums[0]
        maxs = [max_res]
        for i in range(1, n):
            if cur > 0: cur = nums[i] + cur
            else: cur = nums[i]
            max_res = max(cur, max_res)
            maxs.append(max_res)

        cur = nums[-1]
        min_res = nums[-1]
        mins = [min_res]
        for i in range(n-2, -1, -1):
            if cur < 0: cur = nums[i] + cur
            else: cur = nums[i]
            min_res = min(cur, min_res)
            mins.insert(0, min_res)
        res = abs(nums[i] - nums[0])
        for i in range(0, n-1):
            tmp1 = abs(maxs[i] - mins[i+1])
            res = max(res, tmp1)

        cur = nums[-1]
        max_res = nums[-1]
        maxs = [max_res]
        for i in range(n-2, -1, -1):
            if cur > 0: cur = nums[i] + cur
            else: cur = nums[i]
            max_res = max(cur, max_res)
            maxs.insert(0, max_res)

        cur = nums[0]
        min_res = nums[0]
        mins = [min_res]
        for i in range(1, n):
            if cur < 0: cur = nums[i] + cur
            else: cur = nums[i]
            min_res = min(cur, min_res)
            mins.append(min_res)
        for i in range(0, n-1):
            tmp1 = abs(mins[i] - maxs[i+1])
            res = max(res, tmp1)

        return res

    def maxDiffSubArrays(self, nums):
        n = len(nums)
        if n < 2: return -1

        left = [[nums[0], nums[0]]]
        pre_min = pre_max = nums[0]
        l_min = l_max = nums[0]
        for i in range(1, n):
            pre_min = min(pre_min + nums[i], nums[i])
            pre_max = max(pre_max + nums[i], nums[i])
            l_min = min(l_min, pre_min)
            l_max = max(l_max, pre_max)
            left.append([l_min, l_max])

        right = [[nums[-1], nums[-1]]]
        pre_min = pre_max = nums[-1]
        r_min = r_max = nums[-1]
        for i in range(n-2, -1, -1):
            pre_min = min(pre_min + nums[i], nums[i])
            pre_max = max(pre_max + nums[i], nums[i])
            r_min = min(r_min, pre_min)
            r_max = max(r_max, pre_max)
            right.insert(0, [r_min, r_max])

        res = abs(left[0][1] - right[1][0])
        for i in range(n-1):
            res = max(res, abs(left[i][1] - right[i+1][0]),
                      abs(left[i][0] - right[i+1][1]))
        return res

    def maxProduct(self, nums):
        n = len(nums)
        if n <= 0: return 0
        if n == 1: return nums[0]
        pre_min = pre_max = nums[0]
        res = nums[0]
        for i in range(1, n):
            tmp1 = pre_min * nums[i]
            tmp2 = pre_max * nums[i]
            pre_min = min(tmp1, tmp2, nums[i])
            pre_max = max(tmp1, tmp2, nums[i])
            res = max(res, pre_max)
        return res

    def productExceptSelf(self, nums):
        n = len(nums)
        if n <= 1: return []
        left = [nums[0]]
        for i in range(1, n):
            left.append(left[-1] * nums[i])
        right = [nums[-1]]
        for i in range(n-2, -1, -1):
            right.insert(0, right[0] * nums[i])
        res = [right[1]]
        for i in range(n-2):
            res.append(left[i] * right[i+2])
        res.append(left[-2])
        return res






    def subarraySum(self, nums):
        n = len(nums)
        sum = nums[0]
        n_map = {}
        n_map[sum] = 0
        for i in range(1, n):
            sum = sum + nums[i]
            if sum == 0:
                return [0, i]
            if sum in n_map:
                return [n_map[sum]+1, i]
            n_map[sum] = i
        return  None

    def maxTwoSubArrays(self, nums):
        n = len(nums)
        if n <= 1:
            return 0
        left = [nums[0]]
        pre = l_max = nums[0]
        for i in range(1, n):
            pre = max(pre + nums[i], nums[i])
            l_max = max(l_max, pre)
            left.append(l_max)
        right = [nums[-1]]
        pre = r_max = nums[-1]
        for i in range(n-2, -1, -1):
            pre = max(pre + nums[i], nums[i])
            r_max = max(r_max, pre)
            right.insert(0, r_max)

        res = left[0] + right[1]
        for i in range(1, n-1):
            res = max(res, left[i] + right[i+1])
        return res

    def minimumSize(self, nums, s):
        n = len(nums)
        if n == 0:
            return -1
        sums = [0, nums[0]]
        for i in range(1, n):
            sums.append(sums[-1] + nums[i])
        start = 0; end = 1;
        lenth = n+1
        while start < end and (end <= n and start <= n):
            cur = sums[end] - sums[start]
            if cur < s:
                end += 1
            elif cur > s:
                lenth = min(lenth, end-start)
                start += 1
            else:
                lenth = min(lenth, end-start)
                if end == n:
                    start += 1
                else:
                    end += 1
        return lenth if lenth < n+1 else -1






s = Solution()
'''
nums = [1, 3, -1, 2, -1, 2]
nums = [5, 4]
nums = [0,-1]
print(s.maxTwoSubArrays(nums))

nums = [-2,2,-3,4,-1,2,1,-5,3]
print(s.maxSubArray(nums))

nums = [1, -1, -2, 1]
print(s.minimumSubarray(nums))

nums = [-3, 1, 2, -3, 4]
print(s.subarraySum(nums))

nums = [-3, 1, 2, 1]
nums = [1, 2, -3, 1]
print(s.maxDiffSubArrays(nums))

nums = [2, 3, -2, 4]
print(s.maxProduct(nums))

nums = [1, 2, 3, 4]
print(s.productExceptSelf(nums))
'''
nums = [2,3,1,2,4,3]
print(s.minimumSize(nums, 7))

nums = [1, 2, 3, 4, 5]
print(s.minimumSize(nums, 100))
