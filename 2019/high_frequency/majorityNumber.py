class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        n = len(nums)
        res = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i] == res:
                cnt += 1
            else:
                if cnt > 0: cnt -= 1
                else: res = nums[i]
        return res

    def majorityNumberII(self, nums):
        n = len(nums)
        num1 = None; cnt1 = 0
        num2 = None; cnt2 = 0
        for i in range(n):
            if cnt1 == 0:
                num1 = nums[i]
                cnt1 += 1
            elif nums[i] == num1: cnt1 += 1
            elif cnt2 == 0:
                num2 = nums[i]
                cnt2 += 1
            elif nums[i] == num2: cnt2 += 1
            else:
                cnt1 -= 1; cnt2 -= 1
        cnt1 = 0; cnt2 = 0
        for i in range(n):
            if nums[i] == num1:
                cnt1 += 1
            elif nums[i] == num2:
                cnt2 += 1
        return num1 if cnt1 > cnt2 else num2

    def majorityNumberIII(self, nums, k):
        n = len(nums)
        if n <= 0 or n < k:
            return None
        n_map = {}
        for i in range(n):
            if nums[i] in n_map:
                n_map[nums[i]] += 1
            elif len(n_map) < k - 1:
                n_map[nums[i]] = 1
            else:
                tmps = []
                for key in n_map.keys():
                    n_map[key] -= 1
                    if n_map[key] == 0:
                        tmps.append(key)
                for key in tmps:
                    n_map.pop(key)
        for key in n_map.keys():
            n_map[key] = 0
        for i in range(n):
            if nums[i] in n_map:
                n_map[nums[i]] += 1
        res = None; max_cnt = 0
        for key in n_map.keys():
            if n_map[key] > max_cnt:
                res = key; max_cnt = n_map[key]
        return res



s = Solution()
print(s.majorityNumber([1,1,1,1,2,2,2]))
print(s.majorityNumber([1,1,1,2,2,2,2]))
#print(s.majorityNumberII([99,2,99,2,99,3,3]))
print(s.majorityNumberII([1,1,1,1,2,2,3,3,4,4,4]))
print(s.majorityNumberIII([3,1,2,3,2,3,3,4,4,4], 3))
