class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        map = {}
        start = 0; res = 1
        for i in range(n):
            ch = s[i]
            if ch not in map:
                map[ch] = i
                res = max(res, i-start+1)
                continue
            else:
                while map[ch] >= start:
                    start += 1
                map[ch] = i
                res = max(res, i-start+1)
        return res

s = Solution()

print(s.lengthOfLongestSubstring('abcabcbb'))

