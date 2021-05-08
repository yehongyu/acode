class Solution(object):

    def dfs(self, m, n, cnt, x, y, res):
        if cnt <= 0: return
        directs = [[0,-1], [0,1], [-1,0], [1,0]]
        for direct in directs:
            nx = x + direct[0]
            ny = y + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                res[0] += 1
                continue
            self.dfs(m, n, cnt-1, nx, ny, res)

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if m <= 0 or n <= 0: return 0
        if i < 0 or j < 0 or i>=m or j>=n: return 0
        res = [0]
        self.dfs(m, n, N, i, j, res)
        return res[0] % (pow(10,9)+7)

s = Solution()
print(s.findPaths(2,2,2,0,0))
print(s.findPaths(1,3,3,0,1))
