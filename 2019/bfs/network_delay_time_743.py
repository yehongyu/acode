class Solution(object):
    def networkDelayTime(self, times, N, K):
        if K <= 0 or K > N: return -1
        dist = [-1] * (N+1)
        graph = {}
        for time in times:
            u, v, w = time
            if u not in graph: graph[u] = {}
            graph[u][v] = w
        dist[K] = 0
        queue = [K]
        while len(queue) > 0:
            u = queue[0]; queue.pop(0)
            if u not in graph: continue
            for v in graph[u].keys():
                w = graph[u][v]
                if dist[v] == -1 or dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    queue.append(v)
        res = -1
        for i in range(1, N+1):
            if dist[i] == -1: return -1
            res = max(res, dist[i])
        return res

s =Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]; N = 4; K = 2
print(s.networkDelayTime(times, N, K))

