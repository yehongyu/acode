import sys
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        res = [1]
        i2 = i3 = i5 = 0
        for i in range(1, n):
            min_num = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
            res.append(min_num)
            if min_num == res[i2] * 2:
                i2 += 1
            if min_num == res[i3] * 3:
                i3 += 1
            if min_num == res[i5] * 5:
                i5 += 1
        print(res)
        return res[n-1]

    def nthSuperUglyNumber(self, n, primes):
        res = [1]
        k = len(primes)
        idxs = [0] * k
        for i in range(1, n):
            min_num = sys.maxsize
            for j in range(k):
                min_num = min(min_num, res[idxs[j]] * primes[j])
            res.append(min_num)
            for j in range(k):
                if res[idxs[j]] * primes[j] == min_num:
                    idxs[j] += 1
        print(res)
        return res[n-1]

    def isHappy(self, n):
        if n <= 0: return False
        if n == 1: return True
        visit = set()
        while n > 1:
            if n in visit:
                return False
            next = 0
            cur = n
            while cur > 0:
                tmp = cur % 10
                next += tmp * tmp
                cur = cur // 10
            visit.add(n)
            n = next
            print(n)
        return n == 1


s = Solution()
#print(s.nthUglyNumber(9))
#print(s.nthSuperUglyNumber(9, [2,3,5]))
print(s.isHappy(19))


