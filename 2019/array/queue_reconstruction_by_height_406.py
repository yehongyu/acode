from functools import cmp_to_key
def cmp(x, y):
    if x[0] != y[0]: return y[0] - x[0]
    else: return x[1] - y[1]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        if n <= 1: return people
        people = sorted(people, key=cmp_to_key(cmp))
        res = []
        for i in range(n):
            res.insert(people[i][1], people[i])
        return res

s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(
    people
))


