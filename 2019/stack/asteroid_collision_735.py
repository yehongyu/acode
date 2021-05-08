class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n = len(asteroids)
        if n <= 1: return asteroids
        stack = []
        for i in range(n):
            if asteroids[i] >= 0: stack.append(asteroids[i])
            elif asteroids[i] < 0:
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < -asteroids[i]:
                    stack.pop(-1)
                if len(stack)>0 and stack[-1]>0 and stack[-1] == -asteroids[i]:
                    stack.pop(-1);
                elif len(stack)>0 and stack[-1] > 0 and stack[-1] > -asteroids[i]:
                    pass
                else:
                    stack.append(asteroids[i])
        res = []
        while len(stack) > 0:
            res.insert(0, stack[-1])
            stack.pop(-1)
        return res

s = Solution()

print(s.asteroidCollision([-2,2,-1,-2]))
