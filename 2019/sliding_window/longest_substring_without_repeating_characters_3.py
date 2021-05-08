#coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        res = 1
        start = 0
        end = 0
        str_map = {}
        while end < len(s):
            while end < len(s) and (s[end] not in str_map or str_map[s[end]] < start):
                str_map[s[end]] = end
                end += 1
            res = max(res, end-start)
            if end < len(s):
                start = str_map[s[end]]+1
                str_map[s[end]] = end
                end += 1
        return res

s = Solution()
print(s.lengthOfLongestSubstring(''))
print(s.lengthOfLongestSubstring('abcabccbb'))
print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring('pwwkew'))


