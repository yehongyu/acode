class Solution:
    """
    @param routes:  a list of bus routes
    @param S: start
    @param T: destination
    @return: the least number of buses we must take to reach destination
    """
    def bfs(self, graph, s, t):
        queue = [[s, 0]]
        visited = set()
        visited.add(s)
        while len(queue) > 0:
            node, dist = queue[0]; queue.pop(0)
            if node not in graph: continue
            for nn in graph[node]:
                if t == nn: return dist + 1
                if nn not in visited:
                    visited.add(nn)
                    queue.append([nn, dist+1])
        return -1

    def numBusesToDestination(self, routes, S, T):
        # Write your code here
        station2bus = {}
        for i in range(len(routes)):
            for sta in routes[i]:
                if sta not in station2bus:
                    station2bus[sta] = []
                station2bus[sta].append(i)
        s_bus = station2bus[S]
        t_bus = station2bus[T]
        graph = {}
        print('sta', station2bus)
        for i in range(len(routes)):
            graph[i] = set()
        for sta in station2bus.keys():
            buses = station2bus[sta]
            if len(buses) >= 2:
                print(buses)
                for i in range(len(buses)):
                    graph[buses[i]].update(buses[0:i] + buses[i+1:])
                    print('gen-graph', i, graph[i])
        res = len(routes) + 1
        print('graph:', graph)
        print('s-t:', s_bus, t_bus)
        for s in s_bus:
            for t in t_bus:
                if s==t: res = 0
                dist = self.bfs(graph, s, t)
                if dist != -1:
                    res = min(res, dist)
        return res+1 if res != len(routes) + 1 else -1

s = Solution()
routes = [[1, 2, 7], [3, 6, 7]]
routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
print(s.numBusesToDestination(routes, 15, 12))


