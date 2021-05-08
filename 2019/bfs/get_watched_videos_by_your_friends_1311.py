from functools import cmp_to_key
def cmp(x, y):
    if x[1] != y[1]: return x[1]-y[1]
    return ord(x[0])-ord(y[0])

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        if level < 0: return []
        if level == 0: return sorted(watchedVideos[id])
        queue = [id]
        n = len(friends)
        visited = [False] * n
        visited[id] = True
        while len(queue) > 0:
            level -= 1
            qlen = len(queue)
            for i in range(qlen):
                cur = queue[0]; queue.pop(0)
                for f in friends[cur]:
                    if visited[f]: continue
                    visited[f] = True
                    queue.append(f)
            if level == 0: break
        map = {}
        qlen = len(queue)
        for f in range(qlen):
            cur = queue[0]; queue.pop(0)
            for video in watchedVideos[cur]:
                if video not in map: map[video] = 0
                map[video] += 1
        items = sorted(map.items(), key=cmp_to_key(cmp))
        res = []
        for item in items:
            res.append(item[0])
        return res
s = Solution()
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]; friends = [[1,2],[0,3],[0,3],[1,2]]; id = 0; level = 1
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]; friends = [[1,2],[0,3],[0,3],[1,2]]; id = 0; level = 2
print(s.watchedVideosByFriends(watchedVideos, friends, id, level))
