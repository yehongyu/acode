class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    def singleNumber(self, A):
        n = len(A)
        res = 0
        for i in range(n):
            res ^= A[i]
        return res

    def XOR(self, res, b):
        n = len(res)
        for i in range(n):
            a = res[i]
            tmp = (b >> i) & 1
            res[i] = (a+tmp) % 3

    def singleNumberII(self, A):
        n = len(A)
        res = [0] * 64
        for i in range(n):
            self.XOR(res, A[i])
        res_num = 0
        for i in range(len(res)):
            res_num += res[i] << i
        return res_num

    def singleNumberIII(self, A):
        n = len(A)
        xor = 0
        for i in range(n):
            xor ^= A[i]
        apart = xor & (-xor)
        a, b = 0, 0
        for i in range(n):
            if A[i] & apart == 0:
                a ^= A[i]
            else:
                b ^= A[i]
        return [a, b]

    def getSingleNumber(self, nums):
        n = len(nums)
        res = nums[0]
        cnt = 1
        for i in range(1, n):
            if nums[i] == res:
                cnt += 1
            else:
                if cnt == 1: return res
                else:
                    res = nums[i]
                    cnt = 1
        return res



s = Solution()
print(s.singleNumber([1,1,1,2,2]))
print(s.singleNumberII([1,1,1,2]))
print(s.singleNumberII([1,2,2,2]))
print(s.singleNumberIII([1,2,2,3,4,4,5,3]))

print(s.getSingleNumber([1,1,1,2,2]))
print(s.getSingleNumber([3,3,2,2,4,5,5]))

