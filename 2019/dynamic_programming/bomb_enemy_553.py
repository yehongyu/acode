class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        if n <= 0: return 0
        row_cnt = 0; col_cnts = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if j==0 or grid[i][j-1] == 'W':
                    row_cnt = 0; k = j
                    while k < n and grid[i][k] != 'W':
                        row_cnt += 1 if grid[i][k] == 'E' else 0
                        k += 1;
                if i == 0 or grid[i-1][j] == 'W':
                    col_cnts[j] = 0; k = i
                    while k < m and grid[k][j] != 'W':
                        col_cnts[j] += 1 if grid[k][j] == 'E' else 0
                        k += 1
                if grid[i][j] == '0':
                    res = max(res, row_cnt + col_cnts[j])
        return res

s = Solution()
grid =[
     "0E00",
     "E0WE",
     "0E00"
]
print(s.maxKilledEnemies(grid))
