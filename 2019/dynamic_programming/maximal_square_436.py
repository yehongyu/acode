class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        m = len(matrix)
        if m <= 0: return 0
        n = len(matrix[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        res = 0
        for i in range(m):
            dp[i][0] = matrix[i][0]
            res = max(res, dp[i][0])
        for j in range(1, n):
            dp[0][j] = matrix[0][j]
            res = max(res, dp[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                res = max(res, dp[i][j])
        return res * res

    def maximalRectangle(self, matrix):




s = Solution()
matrix = [
  [1, 0, 1, 0, 0],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0]
]
print(s.maxSquare(matrix))
