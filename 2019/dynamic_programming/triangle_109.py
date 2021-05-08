import sys
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def __init__(self):
        self.min_path_sum = sys.maxsize

    def helper(self, triangle, x, y, sum):
        if x < 0 or x >= len(triangle) or y < 0 or y >= len(triangle[x]):
            return
        if x == len(triangle) - 1:
            self.min_path_sum = min(self.min_path_sum, sum + triangle[x][y])
            return
        self.helper(triangle, x+1, y, sum + triangle[x][y])
        self.helper(triangle, x+1, y+1, sum + triangle[x][y])

    def minimumTotal_DFS(self, triangle):
        # write your code here
        self.helper(triangle, 0, 0, 0)
        return self.min_path_sum

    def memorySearchHelper(self, triangle, mem, x, y):
        if x == len(triangle)-1:
            mem[x][y] = triangle[x][y]
            return mem[x][y]
        if mem[x][y] != None:
            return mem[x][y]
        if y + 1 >= len(triangle[x+1]):
            mem[x][y] = triangle[x][y] + self.memorySearchHelper(triangle, mem, x+1, y)
        else:
            mem[x][y] = triangle[x][y] + min(self.memorySearchHelper(triangle, mem, x+1, y),
                                        self.memorySearchHelper(triangle, mem, x+1, y+1))
        return mem[x][y]


    def minimumTotal_memory_search(self, triangle):
        if len(triangle) == 0:
            return 0
        mem = []
        for i in range(len(triangle)):
            mem.append([None] * len(triangle[i]))
        return self.memorySearchHelper(triangle, mem, 0, 0)

    def minimumTotal_up2bottow(self, triangle):
        m = len(triangle)
        if m == 0:
            return 0
        dp = []
        for i in range(m):
            dp.append(triangle[i][0:])
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j >= len(triangle[i-1]):
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j], dp[i-1][j-1])
        return min(dp[m-1])

    def minimumTotal_twoDimDP(self, triangle):
        m = len(triangle)
        if m == 0:
            return 0
        dp = []
        for i in range(m):
            dp.append(triangle[i][0:])
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                if j+1 < len(triangle[i+1]):
                    dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                else:
                    dp[i][j] = triangle[i][j] + dp[i+1][j]
        return dp[0][0]

    def minimumTotal(self, triangle):
        m = len(triangle)
        if m == 0:
            return 0
        dp = triangle[m-1][0:]
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]


s = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(s.minimumTotal(triangle))

