class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0: return -1
        acc = 0
        start = 0; end = 0
        min_len = size + 1
        while start < size:
            if acc < s and end < size:
                acc += nums[end]
                end += 1
            elif start < size:
                if acc >= s:
                    min_len = min(end-start, min_len)
                acc -= nums[start]
                start += 1
        if min_len == size+1: return -1
        return min_len

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size <= 1: return 0
        l = 0; r = size-1
        max_area = 0
        while l < r and r < size:
            h = min(height[l], height[r])
            w = r - l
            area = h*w
            max_area = max(max_area, area)
            print("l, r:", l, r)
            print("hei-l, r:", height[l], height[r], area, max_area)
            if height[l] < height[r]: l += 1
            else: r -= 1
        return max_area

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        if size <= 0 or k <= 1: return 0
        l = 0; r = 0; cnt = 0
        prod = 1
        for i in range(size):
            prod *= nums[i]
            while prod >= k:
                prod = prod // nums[l]
                l += 1
            if prod < k:
                cnt += i-l+1
                print(nums[l:i+1])
        return cnt

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        from collections import defaultdict
        map = defaultdict(int); acc = 0; cnt = 0
        map[0] = 1
        for i in range(size):
            acc += nums[i]
            if acc - k in map:
                cnt += map[acc-k]
            map[acc] += 1
            print(i, map, cnt)
        return cnt


    def subarraySumPositive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        l = 0; r = 0; acc = 0; cnt = 0
        while l < size or r < size:
            if r<size and acc <= k:
                acc += nums[r]; r+=1
            else:
                acc -= nums[l]; l+=1
            if acc == k: cnt += 1
            print(acc, l, r)
        return cnt

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        if size <= 0: return None
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if dp[i-num] > 0:
                    dp[i] += dp[i-num]
        return dp[target]



if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1]; k = 2 # res=2
    nums = [1,2,3]; k = 3 # res=2
    print('nums=', nums)
    #res = s.subarraySum(nums, k)
    res = s.subarraySumPositive(nums, k)
    print("sub sum:", res)
    '''
    nums = [10,5,2,6]; k = 100 # res=8
    print('nums=', nums)
    res = s.numSubarrayProductLessThanK(nums, k)
    print("product:", res)
    
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7] # res=49
    height = [2,3,4,5,18,17,6] #17
    res = s.maxArea(height)
    print("height:", res)

    t = 7;
    nums = [2,3,1,2,4,3]
    res = s.minSubArrayLen(t, nums)
    print("min sub array len:", res)
    '''


