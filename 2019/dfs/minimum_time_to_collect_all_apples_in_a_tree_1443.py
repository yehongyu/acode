'''
Post traversal: traverse all nodes
Each node check the time it takes to collect apples in subtree.
Each node returns the time to collects all apples in subtree,
or if not and node contains itself apple return 2, else return 0.


Some of test case where input are not a tree, rather a graph.
(one node has two pareent.) We can build a graph based on the edges input.
So we can use DFS to solve the graph problem.

'''



class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        if len(edges) == 0 or n <= 0: return 0
        all_has_apple = False
        status = [-1] * len(hasApple)
        for i in range(len(hasApple)):
            status[i] = 1 if hasApple[i] else 0
            all_has_apple = all_has_apple and hasApple[i]
        graph = {}
        for f, t in edges:
            if f not in graph: graph[f] = []
            if t not in graph: graph[t] = []
            graph[f].append(t)
            graph[t].append(f)
        print(status, graph)
        has, time = self.dfs(graph, 0, status)
        return time

    def dfs(self, graph, start, status):
        print("start", start, status[start])
        if status[start] == 1: has, time = True, 0
        else: has, time = False, 0
        if start not in graph:
            return has, time
        status[start] = -1
        for node in graph[start]:
            if status[node] >= 0:
                cur_has, cur_time = self.dfs(graph, node, status)
                if cur_has:
                    time += cur_time + 2
                has = has or cur_has
                print('mid:', node, cur_has, cur_time, has, time)
        print("end", start, has, time)
        return has, time

s = Solution()
false = False
true = True
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [false,false,true,false,true,true,false]

edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [false,false,true,false,false,true,false]

edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [false,false,false,false,false,false,false]

n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [false,true,false,false]
res = s.minTime(n, edges, hasApple)
print(res)