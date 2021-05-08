class Solution(object):

    def dfs(self, map, pre, cur, pos):
        if len(pre) == 1: return True
        elif len(cur) == len(pre)-1 or pos>=len(pre)-1:
            return self.dfs(map, cur, '', 0)
        key = pre[pos:pos+2]
        if key not in map: return False
        for ch in map[key]:
            if self.dfs(map, pre, cur+ch, pos+1):
                return True
        return False

    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        map = {}
        for allow in allowed:
            if allow[0:2] not in map:
                map[allow[0:2]] = []
            map[allow[0:2]].append(allow[2])
        return self.dfs(map, bottom, '', 0)

s = Solution()
bottom = 'BCD'; allowed = ["BCG", "CDE", "GEA", "FFF"]
bottom = "AABA"; allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
print(s.pyramidTransition(bottom, allowed))
