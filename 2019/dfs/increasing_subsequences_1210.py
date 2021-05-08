class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """
    def helper(self, nums, res, path, pos):
        n = len(nums)
        if len(path) >= 2:
            res.append(path[0:])
        st = set()
        for i in range(pos, n):
            if len(path) == 0 or path[-1] <= nums[i]:
                if nums[i] in st: continue
                st.add(nums[i])
                path.append(nums[i])
                self.helper(nums, res, path, i+1)
                path.pop(-1)

    def findSubsequences(self, nums):
        # Write your code here
        n = len(nums)
        path = []
        res = []
        self.helper(nums, res, path, 0)
        return res

s = Solution()
print(s.findSubsequences([4,6,7,7]))
#print(s.findSubsequences([65,21,-44,31,-8]))
