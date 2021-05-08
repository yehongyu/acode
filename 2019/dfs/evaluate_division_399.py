class Solution(object):

    def dfs(self, graph, s, e, visited):
        if s not in graph: return -1.0
        if s == e: return 1.0
        for cur in graph[s].keys():
            if cur in visited: continue
            val = graph[s][cur]
            visited.add(cur)
            tmp = self.dfs(graph, cur, e, visited)
            if tmp > 0:
                return val * tmp
        return -1.0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = values[i]
            graph[b][a] = 1/values[i]
        res = []
        for query in queries:
            s, e = query
            if e == '0': val = -1
            elif s == '0': val = 0
            else:
                visited = set()
                visited.add(s)
                val =self.dfs(graph, s, e, visited)
            res.append(val)
        return res

s = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(s.calcEquation(equations, values, queries))