class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1: return n
        str_map = {}
        res = 0
        start = 0; end = 0
        while end < n:
            ch = s[end]
            if ch in str_map and str_map[ch] >= start:
                start = str_map[ch] + 1
            str_map[ch] = end
            res = max(res, end - start + 1)
            print(start, end, res, str_map)
            end += 1
        return res

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('pwwkew'))



