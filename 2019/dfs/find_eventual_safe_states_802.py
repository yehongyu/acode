class Solution(object):

    def dfs(self, graph, pos, state):
        if state[pos] == 0:
            state[pos] = 2
        elif state[pos] == 1: return True
        elif state[pos] == 2: return False
        for next in graph[pos]:
            if not self.dfs(graph, next, state): return False
        state[pos] = 1
        return True
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        if n == 0: return []
        if n==1: return [0]
        state = [0] * n
        res = []
        for i in range(n):
            if self.dfs(graph, i, state):
                res.append(i)
        return res
s=Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(s.eventualSafeNodes(graph))