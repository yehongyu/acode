class Solution(object):
    def helper(self, input, mem):
        n = len(input)
        if n == 0: return [0]
        if input.isdigit(): return [int(input)]
        if input in mem: return mem[input]
        res = []
        for i in range(1, n-1):
            if input[i] in ['+', '-', '*']:
                left = self.helper(input[0:i], mem)
                right = self.helper(input[i+1:], mem)
                for l_val in left:
                    for r_val in right:
                        if input[i] == '+': res.append(l_val + r_val)
                        elif input[i] == '-': res.append(l_val - r_val)
                        elif input[i] == '*': res.append(l_val * r_val)
        mem[input] = res
        return res

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        n = len(input)
        if n == 0: return [0]
        if input.isdigit(): return [int(input)]
        mem = {}
        return self.helper(input, mem)

s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))
