class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def getNextWord(self, dict, word):
        res = []
        for cur in dict:
            if cur == word: continue
            cnt = 0; i = 0
            while i < len(word):
                if word[i] != cur[i]:
                    cnt += 1
                i += 1
            if cnt == 1: res.append(cur)
        return res

    def ladderLength(self, start, end, dict):
        # write your code here
        if len(start) != len(end):
            return 0
        dict.append(end)
        queue = []
        visited = set()
        queue.append([start, 1])
        while len(queue) > 0:
            cur, level = queue[0]
            queue.pop(0)
            visited.add(cur)
            tmps = self.getNextWord(dict, cur)
            for tmp in tmps:
                if tmp == end: return level + 1
                if tmp in visited: continue
                if tmp in dict:
                    queue.append([tmp, level+1])
        return 0

s = Solution()
print(s.ladderLength("a", "c", ["a", "b", "c"]))
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
