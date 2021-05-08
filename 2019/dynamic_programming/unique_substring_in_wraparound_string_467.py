class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        n = len(p)
        if n <= 1: return n
        map = {}
        map[p[0]] = 1
        pre = 1
        for i in range(1, n):
            cur = 1
            if ord(p[i])- ord(p[i-1]) == 1 or (p[i]=='a' and p[i-1]=='z'):
                cur = pre + 1
            if p[i] not in map:
                map[p[i]] = 0
            map[p[i]] = max(map[p[i]], cur)
            pre = cur
        return sum(map.values())

s = Solution()
print(s.findSubstringInWraproundString('zab'))
