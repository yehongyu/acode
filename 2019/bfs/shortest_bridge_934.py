class Solution(object):

    def dfs(self, A, arr, i, j):
        m = len(A); n = len(A[0])
        directs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for direct in directs:
            nx = i + direct[0]
            ny = j + direct[1]
            if nx<0 or nx>=m or ny<0 or ny>=n: continue
            if A[nx][ny] != 1: continue
            A[nx][ny] = 2; arr.append([nx, ny])
            self.dfs(A, arr, nx, ny)

    def min_path_find_first_1_bfs(self, A, queue):
        res = 0
        m = len(A); n = len(A[0])
        directs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        while len(queue) > 0:
            qlen = len(queue)
            res += 1
            for i in range(qlen):
                x, y = queue[0]; queue.pop(0)
                for direct in directs:
                    nx = x + direct[0]
                    ny = y + direct[1]
                    if nx<0 or nx>=m or ny<0 or ny>=n: continue
                    if A[nx][ny] == 1:
                        return res-1
                    if A[nx][ny] != 0: continue
                    A[nx][ny] = 2
                    queue.append([nx, ny])

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        if m == 0: return -1
        n = len(A[0])
        if n == 0: return -1
        arr = []
        flag = False
        for i in range(m):
            if flag: break
            for j in range(n):
                if flag: break
                if A[i][j] == 1:
                    flag = True
                    A[i][j] = 2; arr.append([i, j])
                    self.dfs(A, arr, i, j)
        return self.min_path_find_first_1_bfs(A, arr)

s = Solution()
A = [[0,1,0],[0,0,0],[0,0,1]]
A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
A = [[0,1], [1,0]]
print(s.shortestBridge(A))
