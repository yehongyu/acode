class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {0: -1}
        n = len(s)
        if n <= 1: return 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        cur = 0
        res = 0
        for i in range(n):
            if s[i] in vowels:
                tmp = ord(s[i]) - ord('a')
                cur ^= (1 << tmp)
                #print('vowel:', i, s[i], cur)
            if cur not in map:
                map[cur] = i
            else:
                res = max(res, i-map[cur])
            #print('iter:', i, s[i], cur, res, map)
        return res

s = Solution()
print(s.findTheLongestSubstring('eleetminicoworoep'))
print(s.findTheLongestSubstring('leetcodeisgreat'))
print(s.findTheLongestSubstring('bcbcbc'))


