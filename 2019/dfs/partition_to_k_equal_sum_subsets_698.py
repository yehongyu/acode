class Solution(object):


    def dfs(self, nums, target, subset, pos):
        if pos == len(nums):
            for val in subset:
                if val != target: return False
            return True
        uniq = set()
        for j in range(len(subset)):
            if subset[j] + nums[pos] > target: continue
            if subset[j] in uniq: continue
            uniq.add(subset[j])
            subset[j] += nums[pos]
            if self.dfs(nums, target, subset, pos+1): return True
            subset[j] -= nums[pos]
        return False

    def canPartitionKSubsets_dfs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < k: return False
        total = sum(nums)
        if total % k != 0: return False
        target = total / k
        subset = [0] * k
        return self.dfs(nums, target, subset, 0)

    def dfs2(self, nums, target, k, visited, cur_sum):
        if k == 1: return True
        if cur_sum == target:
            return self.dfs2(nums, target, k-1, visited, 0)
        for i in range(len(nums)):
            if nums[i] + cur_sum > target: continue
            if visited[i]: continue
            visited[i] = True
            if self.dfs2(nums, target, k, visited, cur_sum + nums[i]): return True
            visited[i] = False
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < k: return False
        total = sum(nums)
        if total % k != 0: return False
        target = total / k
        visited = [False] * len(nums)
        return self.dfs2(nums, target, k, visited, 0)


s = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]; k = 4
print(s.canPartitionKSubsets(nums, k))