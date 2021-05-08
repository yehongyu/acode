#coding=utf-8
import random

# The rand7() API is already defined for you.
# @return a random integer in the range 1 to 7
def rand7():
    return random.randint(1, 7)

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1 ) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1


s = Solution()
print(s.rand10())
print(s.rand10())
print(s.rand10())

print(rand7())
print(rand7())
print(rand7())
