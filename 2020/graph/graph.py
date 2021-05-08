"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None: return None
        node_map = {}
        node_map[node] = Node(node.val)
        queue = [node]
        while len(queue) > 0:
            cur = queue.pop(0)
            for n in cur.neighbors:
                if n not in node_map:
                    node_map[n] = Node(n.val)
                    queue.append(n)
                node_map[cur].neighbors.append(node_map[n])
        return node_map[node]


    def canFinish_dfs(self, graph, visited, start):
        if visited[start] == 1:
            return True
        if visited[start] == 2:
            return False
        visited[start] = 1
        if start in graph:
            for n in graph[start]:
                if self.canFinish_dfs(graph, visited, n):
                    return True
        visited[start] = 2
        return False


    def canFinish111(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        for edge in prerequisites:
            s, dep = edge
            graph[dep].append(s)
        visited = [0] * numCourses
        for i in range(numCourses):
            if visited[i] == 0:
                has_cycle = self.canFinish_dfs(graph, visited, i)
                if has_cycle: return False
        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for edge in prerequisites:
            s, dep = edge
            graph[dep].append(s)
            indegree[s] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue) >0:
            top = queue.pop(0)
            for n in graph[top]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)
        for i in range(numCourses):
            if indegree[i] != 0:
                return False
        return True

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        import sys
        n = len(heights)
        if n<= 0: return -1
        m = len(heights[0])
        if m==1 and n ==1: return 0
        dp = []
        for i in range(n): dp.append([sys.maxsize] *m)
        dp[0][0] = 0
        queue = [[0,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while len(queue) > 0:
            x, y = queue.pop(0)
            print(x, y, dp[x][y], heights[x][y])
            for direct in directions:
                nx = x + direct[0]
                ny = y + direct[1]
                if nx < 0 or ny < 0 or nx >= n or ny>= m:continue
                cost = abs(heights[nx][ny] - heights[x][y])
                tmp = max(cost, dp[x][y])
                if tmp >= dp[nx][ny]:continue
                dp[nx][ny] = tmp
                queue.append([nx, ny])
        return dp[n-1][m-1]

    def sortColors_helper(self, nums, val, start, end):
        if start >= end:return start
        l = start; r = end
        while l < r:
            while l <= end and nums[l] <= val:
                l += 1
            while r >= start and nums[r] > val:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        if nums[l] <= val: return l + 1
        else: return l

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        pos = self.sortColors_helper(nums, 0, 0, size-1)
        if pos >= size:
            return
        self.sortColors_helper(nums, 1, pos, size-1)

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        size = len(graph)
        from collections import defaultdict
        node_map = defaultdict(set)
        start = 0
        for i in range(size):
            for j in graph[i]:
                start = i
                node_map[i].add(j)
                node_map[j].add(i)
        flag = [0] * size
        for i in range(size):
            if flag[i] != 0: continue
            queue = [i]
            flag[i] = 1
            while len(queue) > 0:
                src = queue.pop(0)
                print(src, node_map, flag)
                for v in node_map[src]:
                    if flag[v] == flag[src]: return False
                    if flag[v] != 0: continue
                    flag[v] = -flag[src]
                    queue.append(v)
        return True

    def allPathsSourceTarget_helper(self, graph, res, path, pos, end, visited):
        if pos == end:
            res.append(path[0:])
            return
        for v in graph[pos]:
            if visited[v] == 0:
                visited[v] = 1
                path.append(v)
                self.allPathsSourceTarget_helper(graph, res, path, v, end, visited)
                path.pop(-1)
                visited[v] = 0

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        size = len(graph)
        if size <= 1: return []
        start = 0; end = size-1
        res = []
        visited = [0] * size
        visited[0] = 1
        path = [0]
        self.allPathsSourceTarget_helper(graph, res, path, start, end, visited)
        return res

    def eventualSafeNodes_BFS(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        size = len(graph)
        if size <= 0: return []
        from collections import defaultdict
        queue = []
        src_map = defaultdict(set)
        for i in range(size):
            if len(graph[i]) == 0:
                queue.append(i)
            for v in graph[i]:
                src_map[v].add(i)
        res = []
        while len(queue) > 0:
            v = queue.pop(0)
            res.append(v)
            for u in src_map[v]:
                graph[u].remove(v)
                if len(graph[u]) == 0:
                    queue.append(u)
            src_map.pop(v)
        return sorted(res)


    def eventualSafeNodes_helper(self, graph, start, state):
        # return is safe
        res = True # be safe
        for v in graph[start]:
            if state[v] in [1, 2]:
                res = False; break
            if state[v] == 3: continue
            if state[v] == 0:
                state[v] = 1
                if not self.eventualSafeNodes_helper(graph, v, state):
                    res = False; break
        if res:
            state[start] = 3
        else: state[start] = 2
        return res

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        size = len(graph)
        if size <= 0: return []
        state = [0] * size
        res = []
        for i in range(size):
            if state[i] == 0:
                state[i] = 1
                self.eventualSafeNodes_helper(graph, i, state)
            if state[i] == 3:
                res.append(i)
        return sorted(res)



def show_graph(node):
    if node == None: return
    queue = [node]
    visited = set()
    visited.add(node)
    while len(queue) > 0:
        size = len(queue)
        for i in range(size):
            top = queue.pop(0)
            print(top.val, "--", end=" ")
            for n in top.neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        print("")


if __name__ == "__main__":
    s = Solution()

    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []] # [4]
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []] # [2,4,5,6]
    res = s.eventualSafeNodes(graph)
    print("safe node:", res)

    '''
    graph = [[1, 2], [3], [3], []]
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    res = s.allPathsSourceTarget(graph)
    print("all path:", res)

    # False
    graph = [[1,2],[0,2],[0,1],[4,5],[3,5],[3,4],[7,8],
             [6],[6],[],[11],[10],[14],[],[12],[16],[15],[],[19,20],[18,20],[18,19],[22,23],[21,23],[21,22],[25,26],[24,26],[24,25],[],[29],[28]]
    # False
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],
             [6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]] # False
    graph = [[1, 3], [0, 2], [1, 3], [0, 2]] # True
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
    graph = [[4],[],[4],[4],[0,2,3]] # True
    res = s.isBipartite(graph)
    print(res)
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node3)
    node4.neighbors.append(node1)

    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    heights = [[1,10,6,7,9,10,4,9]]
    res = s.minimumEffortPath(heights)
    print("min effort path", res)

    numCourses = 2; prerequisites = [[1, 0], [0,1]]
    numCourses = 2; prerequisites = [[1, 0]]
    res = s.canFinish(numCourses, prerequisites)
    print("can finish:", res)
    res = s.cloneGraph(node1)
    show_graph(res)
    print("res:", res.val)
    for n in res.neighbors:
        print("nei:", n.val)
    '''

