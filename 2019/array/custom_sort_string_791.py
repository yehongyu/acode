class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        map = {}
        for ch in T:
            if ch not in map:map[ch]=0
            map[ch] += 1
        res = ''
        for ch in S:
            if ch in map:
                res += ch * map[ch]
                map.pop(ch)
        for ch in map.keys():
            res += ch * map[ch]
        return res

s = Solution()
print(s.customSortString('cba', 'abcd'))
