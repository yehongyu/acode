class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = []
        for i in range(n):
            dist.append([-1] * n)
            dist[i][i] = 0
        for s, e, w in edges:
            dist[s][e] = w
            dist[e][s] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i==j: continue
                    if dist[i][k] == -1 or dist[k][j] == -1: continue
                    if dist[i][j] == -1:
                        dist[i][j] = dist[i][k]+dist[k][j]
                    else:
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        inth = []
        for i in range(n):
            tmp = 0
            for j in range(n):
                if i == j: continue
                if dist[i][j] == -1: continue
                if dist[i][j] <= distanceThreshold:
                    tmp += 1
            inth.append(tmp)
        len_mi = min(inth)
        for i in range(n-1, -1, -1):
            if inth[i] == len_mi:
                return i


s = Solution()
n = 4; edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,8761]]; distanceThreshold = 4
n = 5; edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]; distanceThreshold = 2
print(s.findTheCity(n, edges, distanceThreshold))
