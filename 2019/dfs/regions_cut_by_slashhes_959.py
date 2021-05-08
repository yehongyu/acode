class Solution(object):

    def index(self, x, y, k):
        return (x * self.n + y) * 4 + k

    def find(self, a):
        if a not in self.map:
            self.map[a] = a
            return a
        else:
            while self.map[a] != a:
                a = self.map[a]
            return a
    def union(self, a, b):
        at = self.find(a)
        bt = self.find(b)
        if at != bt:
            self.map[at] = bt
            self.cnt -= 1

    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        self.map = {}
        self.n = len(grid)
        if self.n <= 0: return 0
        self.cnt = 4 * self.n * self.n
        for i in range(self.n):
            for j in range(self.n):
                if i>0:
                    self.union(self.index(i,j,3), self.index(i-1,j,1))
                if j>0:
                    self.union(self.index(i,j,0), self.index(i,j-1,2))
                if grid[i][j] != '/':
                    self.union(self.index(i,j,0), self.index(i,j,1))
                    self.union(self.index(i,j,2), self.index(i,j,3))
                if grid[i][j] != '\\':
                    self.union(self.index(i,j,0), self.index(i,j,3))
                    self.union(self.index(i,j,2), self.index(i,j,1))
        return self.cnt

s = Solution()
grid = [
  " /",
  "/ "
]
print(s.regionsBySlashes(grid))