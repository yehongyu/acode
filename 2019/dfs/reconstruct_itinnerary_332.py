class Solution(object):
    def findItinerary_BFS_Wrong(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if len(tickets) == 0: return []
        graph = {}
        for u, v in tickets:
            if u not in graph: graph[u] = []
            graph[u].append(v)
        queue = ['JFK']
        res = []
        visited = set()
        visited.add('JFK')
        while len(queue) > 0:
            qlen = len(queue)
            print(qlen, queue)
            cur = queue[0]; queue.pop(0)
            for i in range(1, qlen):
                tmp = queue[0]; queue.pop(0)
                if tmp < cur: cur = tmp
            res.append(cur)
            if len(res) >= 2:
                visited.add(res[-2] + '#'+cur)
            if cur not in graph: continue
            for v in graph[cur]:
                key = cur + '#' + v
                print('check', key)
                if key not in visited:
                    print('append', key)
                    queue.append(v)
        return res

    def dfs(self, graph, res, start):
        if start in graph:
            while len(graph[start]) > 0:
                u = graph[start][0]; graph[start].pop(0)
                self.dfs(graph, res, u)
        res.insert(0, start)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        n = len(tickets)
        if n == 0: return []
        graph = {}
        for u, v in tickets:
            if u not in graph: graph[u] = []
            graph[u].append(v)
        for u in graph.keys():
            graph[u] = sorted(graph[u])
        start = 'JFK'
        res = []
        self.dfs(graph, res, start)
        return res


s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(s.findItinerary(tickets))

