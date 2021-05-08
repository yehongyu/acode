class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        n = len(nums)
        if n <= 0 or target < 0: return 0
        if target == 0: return 1
        nums = sorted(nums)
        dp = [0] * (target+1)
        dp[0] = 1
        for j in range(1, target+1):
            for num in nums:
                if j-num >= 0:
                    dp[j] += dp[j-num]
        return dp[target]


    ## use item in inputs
    def backPack(self, m, A):
        n = len(A)
        if n <= 0: return 0
        if m <= 0: return m
        dp = []
        for i in range(n):
            dp.append([False] * (m+1))
            dp[i][0] = True
        for j in range(1, m+1):
            dp[0][j] = j == A[0]
        for i in range(1, n):
            for j in range(1, m+1):
                dp[i][j] |= dp[i-1][j]
                if j-A[i] >= 0:
                    dp[i][j] |= dp[i-1][j-A[i]]
        for j in range(m, -1, -1):
            if dp[n-1][j]:
                return j
        return 0

    def backPackIV(self, A, m):
        n = len(A)
        if n <= 0: return 0
        if m <= 0: return m
        dp = []
        for i in range(n):
            dp.append([0] * (m+1))
            dp[i][0] = 1
        for j in range(1, m+1):
            if j % A[0] == 0:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m+1):
                dp[i][j] += dp[i-1][j]
                if j-A[i] >= 0:
                    dp[i][j] += dp[i][j-A[i]]
        return dp[n-1][m]

    def backPackV(self, A, m):
        n = len(A)
        if n <= 0: return 0
        if m <= 0: return m
        dp = [0] * (m+1)
        dp[0] = 1
        for i in range(0, n):
            for j in range(m, A[i]-1, -1):
                dp[j] += dp[j-A[i]]
        return dp[m]

    def backpackIX(self, n, prices, probability):
        m = len(prices)
        if m <= 0 or n <= 0: return 0
        dp = [1] * (n+1)
        for i in range(m):
            for j in range(n, prices[i]-1, -1):
                dp[j] = min(dp[j], dp[j-prices[i]] * (1.0 - probability[i]))
        return 1.0 - dp[n]

    def backPackII(self, m, A, V):
        n = len(A)
        if n <= 0 or m <= 0: return 0
        dp = []
        for i in range(n):
            dp.append([0] * (m+1))
        for j in range(A[0], m+1):
            dp[0][j] = V[0]
        print(0, dp[0])
        for i in range(1, n):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j]
                if j-A[i] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-A[i]]+V[i])
            print(i, dp[i])
        return dp[n-1][m]

    def backPackII_1D(self, m, A, V):
        n = len(A)
        if n <= 0 or m <= 0: return 0
        dp = [0] * (m+1)
        for i in range(n):
            for j in range(m, A[i]-1, -1):
                dp[j] = max(dp[j], dp[j-A[i]]+V[i])
            print(i, dp)
        return dp[m]



s = Solution()
m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
m =200
A = [79,58,86,11,28,62,15,68]
V = [83,14,54,79,72,52,48,62]
print(s.backPackII(m, A, V))
'''
n = 10
pricees = [4, 4, 5,]
probability = [0.1, 0.2, 0.3]
print(s.backpackIX(n, pricees, probability))

nums = [1, 2, 3, 3, 7]
target = 7
print(s.backPackV(nums, target))

nums = [2, 3, 6, 7]
target = 7
print(s.backPackIV(nums, target))

nums = [3, 4, 6]
target = 8
print(s.backPack(target, nums))

nums = [1,2,4]
target = 4
print(s.backPackVI(nums, target))
'''
