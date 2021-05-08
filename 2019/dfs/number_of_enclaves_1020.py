class Solution(object):
    def dfs(self, A, x, y):
        m = len(A)
        n = len(A[0])
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if A[nx][ny] == 0: continue
            A[nx][ny] = 0
            self.dfs(A, nx, ny)

    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        if m <= 0: return 0
        n = len(A[0])
        for i in range(m):
            if A[i][0] == 1:
                A[i][0] = 0
                self.dfs(A, i, 0)
            if A[i][n-1] == 1:
                A[i][n-1] = 0
                self.dfs(A, i, n-1)
        for j in range(1, n-1):
            if 1<m and A[0][j] == 1:
                A[0][j] = 0
                self.dfs(A, 0, j)
            if m-1>=0 and A[m-1][j] == 1:
                A[m-1][j] = 0
                self.dfs(A, m-1, j)
        res = 0
        for i in range(m):
            for j in range(n):
                res += A[i][j]
        return res

s = Solution()
A = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
print(s.numEnclaves(A))

