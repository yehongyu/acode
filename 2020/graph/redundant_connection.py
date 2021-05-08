class Solution(object):
    def findRedundantConnection_BFS(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        n = len(edges)
        if n <= 0: return []
        if n == 1: return edges[0]
        graph = defaultdict(set)
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)
        queue = []
        for i in range(1, n+1):
            if len(graph[i]) <= 1:
                queue.append(i)
        while len(queue) > 0:
            src = queue.pop(0)
            for v in graph[src]:
                graph[v].remove(src)
                if len(graph[v]) <= 1:
                    queue.append(v)
            graph.pop(src)
        for i in range(n-1, -1, -1):
            u, v = edges[i]
            if v in graph[u]:
                return [u, v]

    def findRedundantConnection_hasCycle_BFS(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        size = len(edges)
        if size <= 0: return []
        if size == 1: return edges[0]
        graph = defaultdict(set)
        for i in range(size):
            u, v = edges[i]
            #self.hasCycle_DFS(u, v, graph, pre)
            #BFS
            queue = [u]
            visited = set([u]) # node in visited, has tested if has cycle with v
            while len(queue) > 0:
                top = queue.pop(0)
                if v in graph[top]: return [u, v]
                for next in graph[top]:
                    if next not in visited:
                        queue.append(next)
                        visited.add(next)
            graph[u].add(v)
            graph[v].add(u)


    def has_cycle_dfs(self, u, v, graph, visited):
        if v in graph[u]: return True
        for next in graph[u]:
            if next in visited: continue
            visited.add(next)
            if self.has_cycle_dfs(next, v, graph, visited):
                return True
        return False

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        size = len(edges)
        if size <= 0: return []
        if size == 1: return edges[0]
        graph = defaultdict(set)
        for i in range(size):
            u, v = edges[i]
            visited = set([u])
            if self.has_cycle_dfs(u, v, graph, visited):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict
        size = len(edges)
        if size <= 0: return []
        if size == 1: return edges[0]
        father = defaultdict(set)
        child = defaultdict(set)
        outdegree = defaultdict(int)
        indegree = defaultdict(int)
        for edge in edges:
            u, v = edge
            father[v].add(u)
            child[u].add(v)
            outdegree[u] += 1
            indegree[v] += 1
        queue = []
        # find node which's indegree >=2
        second = None
        print("ori father:", father)
        print("ori child:", child)
        for i in range(1, size+1):
            if len(father[i]) > 1:
                second = i
            if outdegree[i] == 0 or len(father[i]) == 0:
                queue.append(i)
        # has cycle or not
        while len(queue) > 0:
            top = queue.pop(0)
            for src in father[top]:
                outdegree[src] -= 1
                print("top, child", top, child[top])
                child[src].remove(top)
                if outdegree[src] == 0:
                    queue.append(i)
            print("top", top, father)
            father.pop(top)
            for dest in child[top]:
                indegree[dest] -= 1
                father[dest].remove(top)
                if indegree[dest] == 0:
                    queue.append(i)
            child.pop(top)
            print("top child", top, child)
        print("father:", father)
        for i in range(size-1, -1, -1):
            u, v = edges[i]
            if second != None and v != second: continue
            if u in father[v]:
                return [u, v]
        for i in range(size-1, -1, -1):
            u, v = edges[i]
            if v == second: return [u, v]

    def accountsMerge_helper(self, accounts, visited, emails):
        n = len(accounts)
        for i in range(n):
            if visited[i] != 0: continue
            if len(emails & set(accounts[i][1:])) > 0:
                visited[i] = 1
                emails.update(accounts[i][1:])
                self.accountsMerge_helper(accounts, visited, emails)

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        visited = [0] * n
        res = []
        for i in range(n):
            if visited[i] == 0:
                visited[i] == 1
                name = accounts[i][0]
                emails = set(accounts[i][1:])
                self.accountsMerge_helper(accounts, visited, emails)
                res.append([name] + sorted(list(emails)))
        return res

    def networkDelayTime_BFS(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        size = len(times)
        if N < 0 or size < N-1 or K > N or K <= 0: return -1
        if N == 1: return 0
        from collections import defaultdict
        graph = defaultdict(dict)
        for time in times:
            u, v, w = time
            graph[u][v] = w
        queue = [K]
        import sys
        distance = [sys.maxsize] * (N+1)
        distance[K] = 0
        while len(queue) > 0:
            src = queue.pop(0)
            for v in graph[src].keys():
                w = graph[src][v]
                if distance[src] + w < distance[v]:
                    distance[v] = distance[src] + w
                    queue.append(v)
        res = -1
        for i in range(1, N+1, 1):
            if i == K: continue
            if distance[i] == sys.maxsize:
                return -1
            res = max(res, distance[i])
        return res

    def networkDelayTime_DFS_helper(self, graph, distance, src):
        for v in graph[src].keys():
            w = graph[src][v]
            if w + distance[src] < distance[v]:
                distance[v] = w + distance[src]
                self.networkDelayTime_DFS_helper(graph, distance, v)

    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        size = len(times)
        if N < 0 or size < N-1 or K > N or K <= 0: return -1
        if N == 1: return 0
        from collections import defaultdict
        graph = defaultdict(dict)
        for time in times:
            u, v, w = time
            graph[u][v] = w
        import sys
        distance = [sys.maxsize] * (N+1)
        distance[K] = 0
        self.networkDelayTime_DFS_helper(graph, distance, K)
        res = -1
        for i in range(1, N+1, 1):
            if i == K: continue
            if distance[i] == sys.maxsize:
                return -1
            res = max(res, distance[i])
        return res









if __name__ == "__main__":
    s = Solution()

    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4; K = 2
    res = s.networkDelayTime(times, N, K)
    print(res)
    '''
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    res = s.accountsMerge(accounts)
    for val in res: print(val)
    
    edges = [[1,2], [1,3], [2,3]] # [2,3]
    edges = [[2, 1], [3, 1], [4, 2], [1, 4]] # [2,1]
    edges = [[1,2], [2,3], [3,4], [4,1], [1,5]] # [4,1]
    res = s.findRedundantDirectedConnection(edges)
    print("redundant:", res)
    edges = [[1,2], [1,3], [2,3]]
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    res = s.findRedundantConnection(edges)
    print("redundant:", res)
    '''



