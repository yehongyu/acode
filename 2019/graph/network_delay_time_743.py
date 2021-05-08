import sys
class Solution(object):
    def networkDelayTime_Queue(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = {}
        for time in times:
            s, e, w = time
            if s not in graph:
                graph[s] = {}
            graph[s][e] = w
        dist = [sys.maxsize] * (N+1)
        queue = [K]
        dist[K] = 0
        while len(queue) > 0:
            visited = set()
            qlen = len(queue)
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                if cur in graph:
                    print(cur, graph[cur])
                    for e in graph[cur].keys():
                        if dist[cur] + graph[cur][e] < dist[e]:
                            dist[e] = min(dist[e], dist[cur] + graph[cur][e])
                            if e not in visited:
                                queue.append(e)
                                visited.add(e)
        res = max(dist[1:])
        print(dist)
        if res == sys.maxsize: return -1
        return res

    def networkDelayTime(self, times, N, K):
        dist = [sys.maxsize] * (N+1)
        dist[K] = 0
        for i in range(1, N):
            for e in times:
                u, v, w = e
                if dist[u] != sys.maxsize and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        res = max(dist[1:])
        if res == sys.maxsize: return -1
        return res




s = Solution()
times = [[1,2,1],[2,1,3]]; N = 2; K = 2
times = [[2,1,1],[2,3,1],[3,4,1]]; N = 4; K = 2
times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
N = 5
K = 3
print(s.networkDelayTime(times, N, K))


