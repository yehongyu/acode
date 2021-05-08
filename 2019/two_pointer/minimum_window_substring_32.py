class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow_old(self, source , target):
        # write your code here
        n = len(source)
        m = len(target)
        if n < m: return None
        c_map = {}
        for c in source:
            c_map[c] = 0
        for c in target:
            if c not in c_map:
                return None
            c_map[c] += 1
        cnt = 0; left = 0; maxlen = n; res = None
        for i in range(n):
            c = source[i]
            c_map[c] -= 1
            if c_map[c] >= 0: cnt += 1
            while cnt == m:
                curlen = i - left - 1
                if curlen < maxlen:
                    maxlen = curlen
                    res = source[left:i+1]
                c_map[source[left]] += 1
                if c_map[source[left]] > 0: cnt -= 1
                left += 1
        return res

    def minWindow(self, source , target):
        m = len(source)
        n = len(target)
        map = {}
        for ch in source:
            map[ch] = 0
        for ch in target:
            if ch not in map:
                return -1
            map[ch] += 1
        cnt = 0; start = 0
        res = source
        for i in range(m):
            ch = source[i]
            map[ch] -= 1
            if map[ch] >= 0:
                cnt += 1
            while start <= i and cnt == n:
                if len(res) > i-start+1:
                    res = source[start:i+1]
                map[source[start]] += 1
                if map[source[start]] > 0: cnt -= 1
                start += 1
        return res

s = Solution()
print(s.minWindow('abc', 'ac'))
print(s.minWindow('adobecodebanc', 'abc'))
