class Solution(object):
    def dfs(self, matrix, state, i, j):
        m = len(matrix)
        n = len(matrix[0])
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        for direct in directs:
            nx = i + direct[0]
            ny = j + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if state[nx][ny]: continue
            if matrix[nx][ny] >= matrix[i][j]:
                state[nx][ny] = True
                self.dfs(matrix, state, nx, ny)

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        pacific = []
        atlantic = []
        for i in range(m):
            pacific.append([False] * n)
            atlantic.append([False] * n)
            pacific[i][0] = True
            atlantic[i][-1] = True
        for j in range(n):
            pacific[0][j] = True
            atlantic[-1][j] = True
        for i in range(m):
            self.dfs(matrix, pacific, i, 0)
            self.dfs(matrix, atlantic, i, n-1)
        for j in range(n):
            self.dfs(matrix, pacific, 0, j)
            self.dfs(matrix, atlantic, m-1, j)
        print(pacific)
        print(atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res


s = Solution()
matrix = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4],
]
print(s.pacificAtlantic(matrix))
