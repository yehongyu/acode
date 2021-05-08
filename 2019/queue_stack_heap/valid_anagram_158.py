class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        n = len(s)
        smap = {}
        for i in range(n):
            if s[i] not in smap:
                smap[s[i]] = 0
            smap[s[i]] += 1
        for i in range(n):
            if t[i] not in smap:
                return False
            smap[t[i]] -= 1
        for k in smap.keys():
            if smap[k] != 0:
                return False
        return True

s = Solution()
print(s.anagram('ab', 'bac'))
print(s.anagram('ab', 'ba'))
