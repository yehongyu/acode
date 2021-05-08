# coding=utf-8

class Solution(object):
    def findRedundantConnection_graph(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) <= 1:
            return edges
        degree_map = {}
        for s, e in edges:
            if s not in degree_map:
                degree_map[s] = []
            degree_map[s].append(e)
            if e not in degree_map:
                degree_map[e] = []
            degree_map[e].append(s)

        queue = []
        for node in degree_map.keys():
            if len(degree_map[node]) == 1:
                queue.append(node)
        while len(queue) > 0:
            node = queue[0]
            queue = queue[1:]
            e = degree_map[node][0]
            degree_map.pop(node)
            degree_map[e].remove(node)
            if len(degree_map[e]) == 0:
                degree_map.pop(e)
            if len(degree_map[e]) == 1:
                queue.append(e)
        res = []
        for s, e in edges:
            if s in degree_map and e in degree_map:
                res = [s, e]
        return res

    def has_cycle(self, start, target, graph, pre):
        if start not in graph:
            return False
        if target in graph[start]:
            return True
        for cur in graph[start]:
            if cur == pre: continue
            if self.has_cycle(cur, target, graph, start): return True
        return False

    def findRedundantConnection_dfs(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for edge in edges:
            if self.has_cycle(edge[0], edge[1], graph, -1):
                return edge
            if edge[0] not in graph: graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if edge[1] not in graph: graph[edge[1]] = []
            graph[edge[1]].append(edge[0])
        return []

    def findRedundantConnection_bfs(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        for edge in edges:
            start = edge[0]; end = edge[1]
            queue = []
            queue.append(start)
            visited = set()
            visited.add(start)
            while (len(queue) > 0):
                node = queue[0]; queue = queue[1:]
                if node not in graph:
                    break
                if end in graph[node]: return edge
                for cur in graph[node]:
                    if cur in visited: continue
                    queue.append(cur)
                    visited.add(cur)
            if start not in graph: graph[start] = []
            graph[start].append(end)
            if end not in graph: graph[end] = []
            graph[end].append(start)
        return []

    def find(self, vec, i):
        while vec[i] != -1:
            i = vec[i]
        return i

    def findRedundantConnection_find_union(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        vec = [-1] * (len(edges)+1)
        for edge in edges:
            start = edge[0]; end = edge[1]
            x = self.find(vec, start)
            y = self.find(vec, end)
            if x == y:
                return edge
            vec[x] = y # union, 建立联系
        return []


s = Solution()
edges = [[1,2], [1,3], [2,3]]
print(s.findRedundantConnection(edges))
edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(s.findRedundantConnection(edges))

