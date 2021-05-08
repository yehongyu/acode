class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 0: return 0
        if size == 1: return nums[0]
        max_sum = nums[0]
        pre = nums[0]
        for i in range(1, size):
            tmp = nums[i]
            if pre >= 0:
                tmp = nums[i] + pre
            max_sum = max(max_sum, tmp)
            pre = tmp
        return max_sum

    def maxSubArray_return_index(self, nums):
        size = len(nums)
        print(nums)
        if size <= 0: return 0
        if size == 1: return nums[0]
        max_sum = nums[0]
        pre = nums[0]
        start = [-1] * size; start[0] = 0
        end = 0
        for i in range(1, size):
            start[i] = i
            tmp = nums[i]
            if pre >= 0:
                tmp = nums[i] + pre
                start[i] = start[i-1]
            if max_sum < tmp:
                end = i
                max_sum = tmp
            print(pre, tmp, start[i], end, max_sum)
            pre = tmp
        return [start[end], end]

    def maxSubArray_TwoSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1: return 0
        if size == 2: return sum(nums)
        pre = nums[0]
        left = [0] * size; left[0] = nums[0]
        for i in range(1, size):
            cur = nums[i]
            if pre > 0:
                cur += pre
            left[i] = max(left[i-1], cur)
            pre = cur
        pre = nums[-1]
        right = [0] * size; right[-1] = nums[-1]
        for i in range(size-2, -1, -1):
            cur = nums[i]
            if pre > 0:
                cur += pre
            right[i] = max(right[i+1], cur)
            pre = cur
        max_sum = sum(nums[0:2])
        for i in range(0, size-1):
            max_sum = max(max_sum, left[i] + right[i+1])
        return max_sum





    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0: return 0
        if size == 1: return nums[0]
        cur_mn = nums[0]
        cur_mx = nums[0]
        max_pro = nums[0]
        for i in range(1, size):
            tmp1 = nums[i] * cur_mx
            tmp2 = nums[i] * cur_mn
            cur_mn = min(nums[i], tmp1, tmp2)
            cur_mx = max(nums[i], tmp1, tmp2)
            max_pro = max(max_pro, cur_mn, cur_mx)
        return max_pro

    def interleavePosNeg(self, nums):
        size = len(nums)
        if size <= 1: return nums
        pos_num = 0; neg_num = 0
        for num in nums:
            if num > 0: pos_num += 1
            elif num < 0: neg_num += 1
            else: []
        if abs(pos_num-neg_num) > 1: return []
        pos_i = 0; neg_i = 1; True
        if neg_num > pos_num:
            pos_i = 1; neg_i = 0;
        while pos_i < size and neg_i < size:
            while pos_i < size and nums[pos_i] > 0:
                pos_i += 2
            while neg_i < size and nums[neg_i] < 0:
                neg_i += 2
            if pos_i < size and neg_i < size:
                nums[pos_i], nums[neg_i] = nums[neg_i], nums[pos_i]
                pos_i += 2; neg_i += 2
        return nums






if __name__ == "__main__":
    s = Solution()

    nums = [-3, 1, 3, -3, 4] # res =[1,4]
    nums = [0, 1, 0, 1] # res = [0, 3]
    nums = [-2,0,0,1,-1,-1] # res = [1,3]
    res = s.maxSubArray_return_index(nums)
    print(res)
    '''
    nums = [1, 3, -1, 2, -1, 2] # res=7
    res = s.maxSubArray_TwoSubarray(nums)
    print(res)
    '''

    '''
    nums = [-1, -2, -3, 4, 5, 6]
    res = s.interleavePosNeg(nums)
    print(res)
    '''

    '''
    nums = [2,3,-2,4]
    nums = [-2,0,-1]
    res = s.maxProduct(nums)
    print("max product:", res)
    '''
    '''
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [-1]
    res = s.maxSubArray(nums)
    print("max sub array:", res)
    '''



