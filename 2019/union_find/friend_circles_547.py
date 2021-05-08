# coding=utf-8

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        if m <= 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(i, m):
                if M[i][j] == 1:
                    self.dfs(M, i, j)
                    res += 1
        return res

    def dfs(self, M, i, j):
        M[i][j] = 0
        for k in range(0, len(M)):
            if M[i][k] == 1 and k != j:
                self.dfs(M, i, k)
            if M[k][j] == 1 and k != i:
                self.dfs(M, k, j)

s = Solution()
M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
print(s.findCircleNum(M))

