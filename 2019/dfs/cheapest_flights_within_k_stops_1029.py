import sys
class Solution:
    """
    @param n: a integer
    @param flights: a 2D array
    @param src: a integer
    @param dst: a integer
    @param K: a integer
    @return: return a integer
    """
    def findCheapestPrice(self, n, flights, src, dst, K):
        # write your code here
        graph = {}
        for i in range(n): graph[i] = []
        for flight in flights:
            s, d, w = flight
            graph[s].append([d, w])
        queue = [[src, 0]]
        dist = [sys.maxsize] * n
        dist[src] = 0
        while len(queue) > 0:
            cur, stop = queue[0]; queue.pop(0)
            if stop > K: continue
            for v, w in graph[cur]:
                cur_w = dist[cur] + w
                if cur_w < dist[v]:
                    dist[v] = cur_w
                    queue.append([v, stop+1])
        return dist[dst] if dist[dst] < sys.maxsize else -1

s = Solution()
flights = [[0,1,100],[1,2,100],[0,2,500]]
print(s.findCheapestPrice(3, flights, 0, 2, 0))

