#coding

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def helper(self, res, path, n, k, start):
        if len(path) == k:
            res.append(path[0:])
            return
        if start > n:
            return
        for i in range(start, n+1):
            path.append(i)
            self.helper(res, path, n, k, i+1)
            path.pop(len(path)-1)



    def combine(self, n, k):
        # write your code here
        if n < 1 or k < 1 or n < k:
            return [[]]
        if n == k:
            return [i for i in range(1, n+1)]
        res = []
        path = []
        self.helper(res, path, n, k, 1)
        return res

s = Solution()
print(s.combine(4, 2))
print(s.combine(4, 1))
