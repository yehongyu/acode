class Solution(object):
    def possibleBipartition_bfs(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if N <= 1: return True
        if len(dislikes) == 0: return True
        graph = {}
        for u, v in dislikes:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        color = [0] * (N+1)
        queue = [u]
        color[u] = 1
        while len(queue) > 0:
            u = queue[0]; queue.pop(0)
            if u not in graph: continue
            for v in graph[u]:
                if color[v] == color[u]: return False
                elif color[v] == 0:
                    color[v] = -color[u]
                    queue.append(v)
        return True

    def dfs(self, graph, pos, color):
        if pos not in graph: return True
        for v in graph[pos]:
            if color[v] == color[pos]: return False
            elif color[v] == 0:
                color[v] = -color[pos]
                if not self.dfs(graph, v, color):
                    return False
        return True

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        if N <= 1: return True
        if len(dislikes) == 0: return True
        graph = {}
        for u, v in dislikes:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        color = [0] * (N+1)
        for i in range(1, N+1):
            if color[i] == 0:
                color[i] = 1
                if not self.dfs(graph, i, color):
                    return False
        return True



s = Solution()
N = 3; dislikes = [[1,2],[1,3],[2,3]]
N = 5; dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
N = 4; dislikes = [[1,2],[1,3],[2,4]]
print(s.possibleBipartition(N, dislikes))