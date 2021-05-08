import math

class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """
    def checkSumOfSquareNumbers(self, num):
        # write your code here
        a = 0
        b = int(math.sqrt(num))
        while a <= b:
            cur = a * a + b * b
            if cur == num:
                return True
            elif cur < num:
                a += 1
            else:
                b -= 1
        return False

s = Solution()
print(s.checkSumOfSquareNumbers(5))
