class Solution(object):

    def bfs(self, red_map, blue_map, is_red, res):
        queue = [0]
        visited = set()
        visited.add('0_'+str(is_red))
        level = 0
        while len(queue) > 0:
            qlen = len(queue)
            level += 1
            for i in range(qlen):
                u = queue[0]; queue.pop(0)
                if is_red and u in red_map:
                    for v in red_map[u]:
                        key = str(v)+'_'+str(is_red)
                        if key not in visited:
                            queue.append(v)
                            visited.add(key)
                            res[v] = level if res[v] == -1 else min(res[v], level)
                            print('red', u, v, res[v])
                if not is_red and u in blue_map:
                    for v in blue_map[u]:
                        key = str(v)+'_'+str(is_red)
                        if key not in visited:
                            queue.append(v)
                            visited.add(key)
                            res[v] = level if res[v] == -1 else min(res[v], level)
                            print('blue', u, v, res[v])
            is_red = not is_red

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0: return []
        red_map = {}
        blue_map = {}
        for edge in red_edges:
            u, v = edge
            if u not in red_map: red_map[u] = []
            red_map[u].append(v)
        for edge in blue_edges:
            u, v = edge
            if u not in blue_map: blue_map[u] = []
            blue_map[u].append(v)
        res = [-1] * n
        res[0] = 0
        self.bfs(red_map, blue_map, True, res)
        print(res)
        self.bfs(red_map, blue_map, False, res)
        print(res)
        return res

s = Solution()
n = 3; red_edges = [[0,1],[1,2]]; blue_edges = []
n = 3; red_edges = [[0,1]]; blue_edges = [[2,1]]
n = 3; red_edges = [[0,1]]; blue_edges = [[1,2]]
n = 3; red_edges = [[0,1],[0,2]]; blue_edges = [[1,0]]
n = 2; red_edges = [[0,1]]; blue_edges = [[1,0]]
n=5; red_edges=[[0,1],[1,2],[2,3],[3,4]]; blue_edges=[[1,2],[2,3],[3,1]]
n=6
red_edges=[[1,5],[2,2],[5,5],[3,0],[4,5],[2,4],[4,1],[1,0],[1,2],[5,2],[2,3],[0,1]]
blue_edges=[[4,4],[2,5],[1,1],[5,4],[3,3]]
print(s.shortestAlternatingPaths(n, red_edges, blue_edges))
