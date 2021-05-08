class Solution(object):
    def isPalind(self, s):
        n = len(s)
        if n <= 1: return True
        l = 0; r = n-1
        while l < r:
            if s[l] != s[r]: return False
            l += 1; r -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n <= 1: return True
        l = 0; r= n-1
        while l < r:
            if s[l] != s[r]:
                return self.isPalind(s[l:r]) or self.isPalind(s[l+1:r+1])
            l += 1; r -= 1
        return True

s = Solution()
print(s.validPalindrome('aba'))
print(s.validPalindrome('abca'))
print(s.validPalindrome('abeca'))
print(s.validPalindrome('abbea'))
