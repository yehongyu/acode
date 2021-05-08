class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump_Forward(self, A):
        n = len(A)
        dp = [False] * (n)
        dp[0] = True
        for i in range(n):
            if not dp[i]: continue
            for j in range(i+1, min(i+A[i]+1, n)):
                dp[j] = True
                if j == n-1: return True
        return False

    def canJump(self, A):
        n = len(A)
        dp = [False] * n
        dp[0] = True
        for i in range(1, n):
            for j in range(i):
                if j + A[j] >= i:
                    dp[i] = True
        return dp[n-1]

    def jump_DP(self, A):
        n = len(A)
        dp = [n+1] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(i):
                if j + A[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)
            print(i, dp[i])
        return dp[n-1] if dp[n-1] <= n else -1

    def jump(self, A):
        n = len(A)
        res = 0
        cur = 0
        i = 0
        while cur < n -1:
            res += 1
            pre = cur
            while i <= pre:
                cur = max(cur, i+A[i])
                i += 1
            if cur == pre: return -1
        return res

    def canReach(self, arr, start):
        n = len(arr)
        queue = [start]
        visited = [False] * n
        visited[start] = True
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                idx = queue[0]; queue.pop(0)
                if arr[idx] == 0: return True
                for factor in [-1, 1]:
                    next = idx + factor * arr[idx]
                    if next >=0 and next<n and not visited[next]:
                        visited[next] = True
                        queue.append(next)
        return False

    def minJumps(self, arr):
        n = len(arr)
        queue = [0]
        visited = [False] * n
        n_map = {}
        for i in range(n):
            if arr[i] not in n_map:
                n_map[arr[i]] = []
            n_map[arr[i]].append(i)
        res = 0
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                idx = queue[0]; queue.pop(0)
                if idx == n-1: return res
                if idx + 1 < n and not visited[idx+1]:
                    visited[idx+1] = True
                    queue.append(idx+1)
                if idx - 1 >= 0 and not visited[idx-1]:
                    visited[idx-1] = True
                    queue.append(idx-1)
                for cur in n_map[arr[idx]]:
                    if cur == idx: continue
                    if not visited[cur]:
                        visited[cur] = True
                        queue.append(cur)
            res += 1
        return -1

    def dfs_mem(self, matrix, dist, x, y):
        if dist[x][y] >= 1:
            return dist[x][y]
        m = len(matrix)
        n = len(matrix[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        val = 1
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]
            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if matrix[x][y] > matrix[nx][ny]:
                cur = self.dfs_mem(matrix, dist, nx, ny)
                val = max(val, cur + 1)
        dist[x][y] = val
        return val

    def longest_path(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dist = []
        for i in range(m):
            dist.append([0] * n)
        res = 0
        for i in range(m):
            for j in range(n):
                cur = self.dfs_mem(matrix, dist, i, j)
                res = max(cur, res)
        return res


s = Solution()
matrix = [
[ 1,  2,  3,  4, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9]
]
print(s.longest_path(matrix))
'''
arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [7]
arr = [7,6,9,6,9,6,9,7]
print(s.minJumps(arr))
arr = [4,2,3,0,3,1,2]
start = 5
start = 0
arr = [3,0,2,1,2]
start = 2
print(s.canReach(arr, start))
A = [2,3,1,1,4]
print(s.jump(A))

A = [3,2,1,0,4]
A = [2,3,1,1,4]
print(s.canJump(A))
'''

