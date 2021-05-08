class Solution:
    """
    @param nums: nums an array of scores
    @return: check if player 1 will win
    """
    def helper(self, nums, start, end):
        if start > end: return 0, 0
        if start == end: return nums[start], 0

        fs_n1, fs_n2 = self.helper(nums, start+1, end)
        fs_cur1 = nums[start] + fs_n2
        fe_n1, fe_n2 = self.helper(nums, start, end-1)
        fe_cur1 = nums[end] + fe_n2
        if fs_cur1 > fe_cur1:
            return fs_cur1, fs_n1
        else:
            return fe_cur1, fe_n1

    def PredictTheWinner_DFS(self, nums):
        # write your code here
        n = len(nums)
        if n <= 0: return False
        if n == 1: return True
        v1, v2 = self.helper(nums, 0, n-1)
        if v1 > v2:
            return True
        return False

    def PredictTheWinner(self, nums):
        n = len(nums)
        if n <= 0: return False
        if n == 1: return True
        dp = []
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        for i in range(n):
            dp.append([0] * n)
            dp[i][i] = nums[i]
        for step in range(2, n+1):
            for i in range(0, n-step+1):
                j = i + step - 1
                print(i, j)
                tmpsum = sums[j+1] - sums[i]
                dp[i][j] = tmpsum - dp[i][j-1]
                dp[i][j] = max(dp[i][j], tmpsum - dp[i+1][j])
        if dp[0][n-1] > sum(nums[0:]) - dp[0][n-1]:
            return True
        return False



s = Solution()
print(s.PredictTheWinner([1,5,2]))


