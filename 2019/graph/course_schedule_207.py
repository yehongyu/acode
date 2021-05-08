class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        ins = [0] * numCourses
        for edge in prerequisites:
            s, dep = edge
            graph[dep].append(s)
            ins[s] += 1
        queue = []
        for i in range(numCourses):
            if ins[i] == 0:
                queue.append(i)
        while len(queue) > 0:
            top = queue[0]; queue.pop(0)
            for i in graph[top]:
                ins[i] -= 1
                if ins[i] == 0:
                    queue.append(i)
        if max(ins) == 0:
            return True
        return False

    def has_circle_dfs(self, graph, visit, start):
        print(start, visit[start], visit, graph)
        if visit[start] == 1: return True
        if visit[start] == -1: return False
        visit[start] = 1
        if start in graph:
            for node in graph[start]:
                if self.has_circle_dfs(graph, visit, node):
                    return True
        visit[start] = -1
        return False

    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for edge in prerequisites:
            s, dep = edge
            if dep not in graph:
                graph[dep] = []
            graph[dep].append(s)
        visit = [0] * numCourses
        print(graph)
        for i in range(numCourses):
            if self.has_circle_dfs(graph, visit, i):
                return False
        return True


    def findOrder(self, numCourses, prerequisites):
        graph = {}
        ins = [0] * numCourses
        for edge in prerequisites:
            s, dep = edge
            if dep not in graph:
                graph[dep] = []
            graph[dep].append(s)
            ins[s] += 1
        queue = []
        for i in range(numCourses):
            if ins[i] == 0:
                queue.append(i)
        res = []
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                top = queue[0]; queue.pop(0)
                res.append(top)
                if top not in graph: continue
                for node in graph[top]:
                    ins[node] -= 1
                    if ins[node] == 0:
                        queue.append(node)
        if max(ins) == 0:
            return res
        return []

    def 



s = Solution()
#print(s.canFinish(2, [[1,0]] ))
#print(s.canFinish(2, [[1,0],[0,1]]))

#print(s.findOrder(2, [[1,0]] ))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
