class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n-1 != len(edges): return False
        if n <= 1: return True
        visited = [0] * n
        indegree = [0] * n
        graph = {}
        for edge in edges:
            s, e = edge
            if s not in graph:
                graph[s] = []
            if e not in graph:
                graph[e] = []
            graph[s].append(e)
            graph[e].append(s)
            indegree[s] += 1
            indegree[e] += 1
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                return False
            if indegree[i] == 1:
                queue.append(i)
        while len(queue) > 0:
            node = queue[0]; queue.pop(0)
            if visited[node]: continue
            visited[node] = 1
            for e in graph[node]:
                indegree[e] -= 1
                if indegree[e] <= 1 and not visited[e]:
                    queue.append(e)
        return min(visited) == 1

s = Solution()
n = 5;
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(s.validTree(n, edges))
