class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * n
        dp[0] = nums[0] > 0
        for i in range(1, n):
            for j in range(i):
                dp[i] |= dp[j] and j+nums[j] >= i
        return dp[n-1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        dp = [n] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return -1 if dp[n-1] == n else dp[n-1]

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        res = set()
        n = len(arr)
        if n <= 0: return False
        if n == 1: return start==0
        if start >= n:
            return False
        queue = [start]
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                top = queue[0]; queue.pop(0)
                res.add(top)
                if arr[top] == 0:
                    return True
                j = top-arr[top]
                if j >=0 and j not in res:
                    queue.append(j)
                j = top+arr[top]
                if j <n and j not in res:
                    queue.append(j)
        return False




s = Solution()
'''
nums = [2, 3, 1, 1, 4]
print(s.canJump(nums))
nums = [2, 3, 1, 1, 0]
print(s.canJump(nums))
nums = [3, 2, 1, 0, 4]
print(s.canJump(nums))
nums = [1, 3, 2]
print(s.canJump(nums))
nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print(s.canJump(nums))
nums = [2, 3, 1, 1, 4]
print(s.jump(nums))
'''
arr = [4,2,3,0,3,1,2]; start = 5
arr = [4,2,3,0,3,1,2]; start = 0
arr = [3,0,2,1,2]; start = 2
arr = [0,3,0,6,3,3,4]; start=6
print(s.canReach(arr, start))
