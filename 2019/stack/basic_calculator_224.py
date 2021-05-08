class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = []
        for ch in s:
            print(ch, res, sign, num)
            if ch.isdigit():
                num = 10 * num + int(ch)
            elif ch in ['+', '-']:
                res = res + sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res = res + sign * num
                num = res
                sign = stack[-1]; stack.pop(-1)
                res = stack[-1]; stack.pop(-1)
                res = res + sign * num
                num = 0
                sign = 1
        res = res + sign * num
        return res

    def calculate_II(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0; num = 0; op = '+'
        stack = []; n = len(s)
        for i in range(n+1):
            if i>= n or s[i] in ['+', '-', '/', '*']:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op in ['*', '/']:
                    if op == '/':
                        if stack[-1] < 0:
                            tmp = -1 * (abs(stack[-1])//num)
                        else:
                            tmp = stack[-1]//num
                    else:
                        tmp = stack[-1] * num
                    stack.pop(-1)
                    stack.append(tmp)
                if i < n:
                    op = s[i]
                    num = 0
            elif s[i].isdigit():
                num = num * 10 + int(s[i])
            print(i, num, stack)
        while len(stack) > 0:
            res += stack[-1]; stack.pop(-1)
        return res


s = Solution()
cal_str = '3 + 2 *2'
cal_str = '14 - 3 /2'
print(s.calculate_II(cal_str))

'''
cal_str = "(1+(4+5+2)-3)+(6+8)"
cal_str = " 2-1 + 2 "
cal_str = "1 + 1"
print(s.calculate(cal_str))
'''


