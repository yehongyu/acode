class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1: return s
        cur = ''; times = 0
        time_stack = []
        str_stack = []
        for i in range(n):
            ch = s[i]
            if ch.isdigit():
                times = times * 10 + int(ch)
            elif ch == '[':
                time_stack.append(times)
                times = 0
                str_stack.append(cur)
                cur = ''
            elif ch == ']':
                cur = cur * time_stack[-1]
                time_stack.pop(-1)
                if len(str_stack) > 0:
                    cur = str_stack[-1] + cur
                    str_stack.pop(-1)
            else:
                cur = cur + ch
            print(i, ch, cur, time_stack, str_stack)
        return cur

s = Solution()
sss = "3[a]2[bc]"
sss = "3[a2[c]]"
sss = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(s.decodeString(sss))
