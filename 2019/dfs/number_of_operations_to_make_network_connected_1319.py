class Solution(object):

    def dfs(self, graph, visited, pos):
        visited[pos] = 1
        if pos in graph:
            for v in graph[pos]:
                if visited[v] == 0:
                    self.dfs(graph, visited, v)
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if n <= 0: return -1
        if len(connections) < n-1: return -1
        graph = {}
        for connect in connections:
            u, v = connect
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        cnt = 0
        visited = [0] * n
        for i in range(n):
            if visited[i] == 0:
                self.dfs(graph, visited, i)
                cnt += 1
        return cnt - 1

s = Solution()
n = 4; connections = [[0,1],[0,2],[1,2]]
n = 5; connections = [[0,1],[0,2],[3,4],[2,3]]
n = 6; connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(s.makeConnected(n, connections))

