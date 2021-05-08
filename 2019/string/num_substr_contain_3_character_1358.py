class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 2: return 0
        left = 0; right = 2
        res = 0
        while left < n and right < n:
            window = s[left:right+1]
            if 'a' in window and 'b' in window and 'c' in window:
                res += n-right
                left += 1
            else:
                right += 1
        return res

s = Solution()
print(s.numberOfSubstrings("abcabc"))
print(s.numberOfSubstrings("aaacb"))
print(s.numberOfSubstrings("abc"))

