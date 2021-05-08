class Solution(object):
    def hammingDistance_recursion(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        val = x ^ y
        if val == 0: return 0
        return val % 2 + self.hammingDistance_recursion(x//2, y//2)

    def hammingDistance(self, x, y):
        val = x ^ y
        res = 0
        while val != 0:
            res += val & 1
            val = val // 2
        return res

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            zero = 0
            for val in nums:
                if val & (1<<i) == 0:
                    zero += 1
            one = len(nums) - zero
            res += one * zero
        return res


if __name__ == "__main__":
    s = Solution()
    #res = s.hammingDistance(4, 14)
    res = s.totalHammingDistance([4, 14, 2, 1])
    print('hamming:', res)