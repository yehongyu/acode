class Solution:
    """
    @param N: size of 2D grid
    @param mines: in the given list
    @return: the order of the plus sign
    """
    def exist(self, matrix, i, j, k):
        n = len(matrix)
        if i-k < 0 or i+k >= n or j-k < 0 or j+k >=n: return False
        res = matrix[i][j-k]
        res += matrix[i][j+k]
        res += matrix[i-k][j]
        res += matrix[i+k][j]
        return res == 4

    def orderOfLargestPlusSign_N3(self, N, mines):
        # Write your code here
        if len(mines) == 0:
            return (N+1) // 2
        matrix = []
        for i in range(N):
            matrix.append([1] * N)
        for i, j in mines:
            matrix[i][j] = 0
        res = 0
        for i in range(N):
            for j in range(N):
                k = 0
                while self.exist(matrix, i, j, k): k+=1
                res = max(k, res)
        return res


    def orderOfLargestPlusSign(self, N, mines):
        # Write your code here
        if len(mines) == 0:
            return (N+1) // 2
        dp = []
        for i in range(N):
            dp.append([-1]*N)
        zeros = set()
        for i, j in mines:
            zeros.add(i*N+j)
        ## from left
        for i in range(N):
            tmp = []
            for j in range(N):
                cur = 0
                if i*N+j not in zeros:
                    cur = 1 if len(tmp) == 0 else tmp[-1] + 1
                tmp.append(cur)
                if dp[i][j] == -1 or cur < dp[i][j]:
                    dp[i][j] = cur
        for i in range(N):
            tmp = []
            for j in range(N-1, -1, -1):
                cur = 0
                if i*N+j not in zeros:
                    cur = 1 if len(tmp) == 0 else tmp[-1] + 1
                tmp.append(cur)
                if dp[i][j] == -1 or cur < dp[i][j]:
                    dp[i][j] = cur
        for j in range(N):
            tmp = []
            for i in range(N):
                cur = 0
                if i*N+j not in zeros:
                    cur = 1 if len(tmp) == 0 else tmp[-1] + 1
                tmp.append(cur)
                if dp[i][j] == -1 or cur < dp[i][j]:
                    dp[i][j] = cur
        for j in range(N):
            tmp = []
            for i in range(N-1, -1, -1):
                cur = 0
                if i*N+j not in zeros:
                    cur = 1 if len(tmp) == 0 else tmp[-1] + 1
                tmp.append(cur)
                if dp[i][j] == -1 or cur < dp[i][j]:
                    dp[i][j] = cur
        res = 0
        for i in range(N):
            for j in range(N):
                res = max(res, dp[i][j])
        return res





s = Solution()
N = 5
mines = [[4, 2]]
print(s.orderOfLargestPlusSign(N, mines))