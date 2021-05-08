class Solution(object):

    def dfs(self, rows, cols, visited, x, y):
        for nx, ny in rows[x]:
            key = str(nx)+'#'+str(ny)
            if key not in visited:
                visited.add(key)
                self.dfs(rows, cols, visited, nx, ny)
        for nx, ny in cols[y]:
            key = str(nx)+'#'+str(ny)
            if key not in visited:
                visited.add(key)
                self.dfs(rows, cols, visited, nx, ny)

    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if len(stones) <= 0: return 0
        rows = {}
        cols = {}
        for x, y in stones:
            if x not in rows: rows[x] = []
            rows[x].append([x, y])
            if y not in cols: cols[y] = []
            cols[y].append([x, y])
        visited = set()
        connect = 0
        for x, y in stones:
            key = str(x)+'#'+str(y)
            if key not in visited:
                visited.add(key)
                self.dfs(rows, cols, visited, x, y)
                connect += 1
        return len(stones)-connect

s = Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(s.removeStones(stones))
