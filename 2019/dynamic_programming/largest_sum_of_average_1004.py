class Solution:
    """
    @param A: an array
    @param K: an integer
    @return: the largest score
    """
    def dfs_mem(self, A, mem, k, pos):
        n = len(A)
        if pos >= n or k==0: return 0
        if mem[pos][k] > 0:
            return mem[pos][k]
        mem[pos][k] = sum(A[pos:]) /float(n-pos)
        if k > 1:
            cur = 0
            for i in range(pos, n):
                cur += A[i]
                val = self.dfs_mem(A, mem, k-1, i+1)
                mem[pos][k] = max(mem[pos][k], cur /float(i-pos+1) + val)
        print(pos, k, mem[pos][k])
        return mem[pos][k]

    def largestSumOfAverages_DFS_MEM(self, A, K):
        # Write your code here
        n = len(A)
        if n<= 0 or K <= 0: return 0
        mem = []
        for i in range(n):
            mem.append([0] * (K+1))
        self.dfs_mem(A, mem, K, 0)
        return mem[0][K]

    def largestSumOfAverages(self, A, K):
        # Write your code here
        n = len(A)
        if n<= 0 or K <= 0: return 0
        dp = []
        sums = [0]
        for i in range(n):
            sums.append(sums[-1] + A[i])
        for i in range(n):
            dp.append([0] * (K))
        for i in range(n):
            dp[i][0] = (sums[n] - sums[i]) / float(n-i)
        for k in range(1, K):
            for i in range(n):
                for j in range(i+1, n):
                    dp[i][k] = max(dp[i][k], (sums[j]-sums[i]) / float(j-i) + dp[j][k-1])
        return dp[0][K-1]


s = Solution()
A = [9, 1, 2, 3, 9]
K = 3
A = [4,1,7,5,6,2,3]
K = 4
print(s.largestSumOfAverages(A, K))