#coding=utf-8

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        def reverse(s, start, end):
            print(start, end, s)
            if start >= end:
                return
            mid = (end-start)/2
            for i in range(mid+1):
                tmp = s[start+i]
                s[start+i] = s[end-i]
                s[end-i] = tmp
        n = len(s)
        if n <= 1:
            return
        offset = offset % n
        if offset <= 0:
            return
        reverse(s, 0, n-offset-1)
        reverse(s, n-offset, n-1)
        reverse(s, 0, n-1)

s = Solution()
sss = 'abcdefg'
s.rotateString(sss, 3)
print(sss)
sss = 'abcdefg'
s.rotateString(sss, 10)
print(sss)
