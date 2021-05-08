class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        if n <= 0: return 0
        graph = {}
        for i in range(len(manager)):
            if manager[i] not in graph: graph[manager[i]] = []
            graph[manager[i]].append(i)
        res = 0
        queue = [[headID, informTime[headID]]]
        while len(queue) > 0:
            u, time = queue[0]; queue.pop(0)
            if u not in graph:
                res = max(res, time)
                continue
            for v in graph[u]:
                queue.append([v, time+informTime[v]])
        return res

s = Solution()
n = 7; headID = 6; manager = [1,2,3,4,5,6,-1]; informTime = [0,6,5,4,3,2,1]
n = 15; headID = 0; manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]; informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
n = 4; headID = 2; manager = [3,3,-1,2]; informTime = [0,0,162,914]
print(s.numOfMinutes(n, headID, manager, informTime))

