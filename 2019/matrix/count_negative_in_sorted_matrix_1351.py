class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return 0
        n = len(grid[0])
        i = m-1; j = 0
        res = 0
        while i>=0 and j<n:
            if grid[i][j] >= 0:
                j += 1
            else:
                res += n-j
                i -= 1
        return res

s = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[3,2],[1,0]]
grid = [[-1]]
print(s.countNegatives(grid))
