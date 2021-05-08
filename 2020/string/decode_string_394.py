
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1: return  s
        stack = []
        val = ''
        for i in range(size):
            cur = s[i]
            print(i, cur, stack, cur)
            if cur == '[':
                if len(val)>0 and val.isdigit():
                    stack.append(int(val))
                    val = ''
            elif cur == ']':
                print('is ]', i, stack, val)
                while len(stack) > 0 and isinstance(stack[-1], str):
                    val = stack[-1] + val
                    stack.pop(-1)
                if len(stack) > 0 and isinstance(stack[-1], int):
                    val = stack[-1] * val
                    stack.pop(-1)
                stack.append(val)
                val = ''
            else:
                if cur.isdigit():
                    if len(val) > 0 and not val.isdigit():
                        stack.append(val)
                        val = ''
                val = val + cur
        if len(val) > 0: stack.append(val)
        print(stack)
        res = ''
        while len(stack) >= 1:
            res = stack[-1] + res
            stack.pop(-1)
        return res

if __name__ == '__main__':
    s = Solution()
    src = "3[a]2[bc]"
    src = "3[a2[c]]"
    src = "abc3[cd]xyz"
    src = "2[abc]3[cd]ef"
    src = "3[a2[c]]"
    res = s.decodeString(src)
    print(src, "===", res)
