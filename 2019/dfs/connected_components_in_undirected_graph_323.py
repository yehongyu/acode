class Solution(object):

    def dfs(self, graph, visited, pos):
        if pos not in graph: return
        for v in graph[pos]:
            if not visited[v]:
                visited[v] = True
                self.dfs(graph, visited, v)

    def countComponents(self, n, edges):
        if n <= 0: return 0
        if len(edges)==0: return n
        visited = [False] * n
        cnt = 0
        graph = {}
        for edge in edges:
            u, v = edge
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                self.dfs(graph, visited, i)
                cnt += 1
        return cnt

s = Solution()
n = 5; edges = [[0, 1], [1, 2], [3, 4]]
n = 5; edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(s.countComponents(n, edges))