class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        if size < 3: return 0
        nums = sorted(A)
        for i in range(size-1, 1, -1):
            first = nums[i]
            second = nums[i-1]
            third = nums[i-2]
            if third + second > first:
                return first + second + third
        return 0

if __name__ == "__main__":
    s = Solution()
    nums = [2,1,2] # 5
    nums = [1,1,2] # 0
    nums = [3,2,3,4] # 10
    res = s.largestPerimeter(nums)
    print("largest:", res)



