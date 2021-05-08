class Solution(object):

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        graph = {}
        degree = [0] * (n+1)
        for s, e in edges:
            if s not in graph: graph[s] = []
            if e not in graph: graph[e] = []
            graph[s].append(e)
            graph[e].append(s)
        queue = []
        for s in graph.keys():
            if len(graph) == 1:
                queue.append(s)
        visited = set()
        while len(queue) > 0:
            node = queue[0]; queue.pop(0)
            if node not in graph: continue
            for e in graph[node]:
                graph[e] -= 1

