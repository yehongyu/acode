class Solution(object):

    def helper(self, s, pos, left_cnt, right_cnt):
        if left_cnt < right_cnt: return False
        if pos == len(s): return left_cnt == right_cnt
        if s[pos] == '(':
            return self.helper(s, pos+1, left_cnt+1, right_cnt)
        elif s[pos] == ')':
            return self.helper(s, pos+1, left_cnt, right_cnt+1)
        else:
            if self.helper(s, pos+1, left_cnt+1, right_cnt): return True
            elif self.helper(s, pos+1, left_cnt, right_cnt+1): return True
            else:
                return self.helper(s, pos+1, left_cnt, right_cnt)
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.helper(s, 0, 0, 0)

s = Solution()

print(s.checkValidString('((*))'))
print(s.checkValidString('())'))
