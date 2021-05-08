#coding=utf-8

class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr_loop(self, source, target):
        # Write your code here
        n = len(source)
        m = len(target)
        for i in range(n-m+1):
            flag = True
            for j in range(m):
                if source[i+j] != target[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1

    def findnext(self, s):
        n = len(s)
        vec = [-1] * n
        k = 0
        for i in range(1, n):
            k = vec[i-1]
            while k > -1:
                if s[k] == s[i-1]:
                    vec[i] = k + 1
                    break
                else:
                    k = vec[k]
            if k == -1:
                vec[i] = 0
        return vec

    def strStr(self, source, target):
        n = len(source)
        m = len(target)
        if m <= 0:
            return 0
        if n < m:
            return -1
        print(source, target)
        vec = self.findnext(target)
        print(vec)
        i = 0
        j = 0
        while i < n and j < m:
            if j == -1 or (i < n and j < m and source[i] == target[j]):
                i += 1; j += 1
            else:
                j = vec[j]
        if j == m:
            return i - j
        else:
            return -1




s = Solution()
print(s.strStr('source', 'target')) # -1
print(s.strStr('abcabcdef', 'abcd')) # 3
print(s.strStr('abcabcdef', 'abcdabce'))
print(s.strStr('abcabcdef', 'abcdabre'))
print(s.strStr('abcde', 'e'))
