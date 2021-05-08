class Solution(object):

    def dfs(self, graph, quiet, res, pos):
        if res[pos] >= 0:
            return res[pos]
        res[pos] = pos
        if pos in graph:
            for v in graph[pos]:
                pv = self.dfs(graph, quiet, res, v)
                if quiet[pv] < quiet[res[pos]]:
                    res[pos] = pv
        return res[pos]

    def loudAndRich_dfs(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        graph = {}
        for u, v in richer:
            if v not in graph: graph[v] = []
            graph[v].append(u)
        print(graph)
        res = [-1] * n
        for i in range(n):
            self.dfs(graph, quiet, res, i)
        return res

    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        graph = {}
        res = [-1] * n
        indegree = [0] * n
        for u, v in richer:
            if u not in graph: graph[u] = []
            graph[u].append(v)
            indegree[v] += 1
        queue = []
        for i in range(n):
            if indegree[i] == 0: queue.append(i)
            res[i] = i
        while len(queue) > 0:
            u = queue[0]; queue.pop(0)
            if u not in graph: continue
            for v in graph[u]:
                if quiet[res[v]] > quiet[res[u]]:
                    res[v] = res[u]
                indegree[v] -= 1
                if indegree[v] == 0: queue.append(v)
        return res





s = Solution()
richer = [[0,1]]
quiet = [1,2,0]

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]

print(s.loudAndRich(richer, quiet))
