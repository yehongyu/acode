class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        queue = [0]
        res = set()
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(qlen):
                top = queue[0]; queue.pop(0)
                if top not in res:
                    res.add(top)
                    for node in rooms[top]:
                        queue.append(node)
        print(res)
        return len(res) == len(rooms)

s = Solution()
rooms = [[1],[2],[3],[]]
print(s.canVisitAllRooms(rooms))
