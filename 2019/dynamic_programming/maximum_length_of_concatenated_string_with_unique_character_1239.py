class Solution(object):

    def countBits(self, num):
        cnt = 0
        while num > 0:
            if num & 1:
                cnt += 1
            num = num >> 1
        return cnt

    def dfs(self, nums, start, cur_mask, res):
        res[0] = max(res[0], self.countBits(cur_mask))
        for i in range(start, len(nums)):
            if cur_mask & nums[i] == 0:
                self.dfs(nums, i+1, cur_mask|nums[i], res)

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        n = len(arr)
        nums = []
        for val in arr:
            tmp = 0
            for ch in val:
                cur = (ord(ch.lower())-ord('a'))
                if (tmp >> cur) & 1 == 1:
                    tmp = 0
                    break
                tmp |= 1<<cur
            if tmp != 0:
                nums.append(tmp)
        res = [0]
        self.dfs(nums, 0, 0, res)
        return res[0]

s = Solution()
print(s.maxLength(["un","iq","ue"]))
print(s.maxLength(["cha","r","act","ers"]))


