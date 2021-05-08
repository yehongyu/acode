class Solution(object):
    def findCheapestPrice_DFS(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for flight in flights:
            u, v, w = flight
            if u not in graph: graph[u] = {}
            graph[u][v] = w
        dist = [-1] * n
        dist[src] = 0
        queue = [src]
        step = 0
        print(graph)
        while len(queue) > 0:
            qlen = len(queue)
            step += 1
            if step > K+1: break
            for i in range(qlen):
                u = queue[0]; queue.pop(0)
                if u not in graph: continue
                for v in graph[u].keys():
                    if dist[v]==-1 or dist[v] > dist[u]+graph[u][v]:
                        dist[v] = dist[u]+graph[u][v]
                        queue.append(v)
                    print(step, u, v, dist)
        return dist[dst]

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        import sys
        dp = [-1] * n
        dp[src] = 0
        for i in range(K+1):
            tmp_dp = dp[0:]
            for flight in flights:
                u, v, w = flight
                if dp[u] != -1:
                    if tmp_dp[v] == -1:
                        tmp_dp[v] = dp[u]+w
                    else:
                        tmp_dp[v] = min(tmp_dp[v], dp[u]+w)
            dp = tmp_dp[0:]
            print(i, dp)
        return dp[dst]


s = Solution()
n = 3; edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0; dst = 2; k = 0

n = 7
edges = [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]]
src = 2
dst = 4
k = 1
n=5
edges=[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
src=0
dst=4
k=1
print(s.findCheapestPrice(n, edges, src, dst, k))


