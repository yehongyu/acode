class Solution(object):
    def canFinishBFS(self, numCourses, prerequisites):
        graph = {}
        indegree = [0] * numCourses
        for prere in prerequisites:
            u, v = prere
            if v not in graph: graph[v] = set()
            graph[v].add(u)
            indegree[u] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        print(indegree)
        print(graph)
        while len(queue) > 0:
            u = queue[0]; queue.pop(0)
            if u not in graph: continue
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        for i in range(numCourses):
            if indegree[i] != 0: return False
        return True

    # DFS
    def has_cycle_dfs(self, graph, visited, pos):
        visited[pos] = 1
        if pos in graph:
            for v in graph[pos]:
                if visited[v] == 1: return True
                elif visited[v] == 2: continue
                if self.has_cycle_dfs(graph, visited, v):
                    return True
        visited[pos] = 2
        return False

    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for prere in prerequisites:
            u, v = prere
            if v not in graph: graph[v] = []
            graph[v].append(u)
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                if self.has_cycle_dfs(graph, visited, i):
                    return False
        return True

s = Solution()
numCourses = 2; prerequisites = [[1,0],[0,1]]
numCourses = 2; prerequisites = [[1,0]]
print(s.canFinish(numCourses, prerequisites))

