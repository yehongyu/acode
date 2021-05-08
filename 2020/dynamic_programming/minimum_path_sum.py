class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0: return -1
        n = len(grid[0])
        dp = []
        import sys
        for i in range(m): dp.append([sys.maxsize] * n)
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]

    # Determine if you are able to reach the last index.
    def canJump_DP(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size <= 1: return True
        dp = [False] * size
        dp[0] = True
        for i in range(1, size):
            for j in range(0, i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]

    # Determine if you are able to reach the last index.
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size <= 1: return True
        start = 0
        while start < size-1:
            if nums[start] == 0:
                return False
            end = start + nums[start]
            i = start + 1
            while i <= end and i < size:
                if i + nums[i] > end:
                    end = i + nums[i]
                i += 1
            start = end
        return True

    # minimum times of jumps to last index from first index
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 1: return 0
        dp = [size+1] * size
        dp[0] = 0
        for i in range(1, size):
            for j in range(0, i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)
        if dp[-1] == size+1:
            return -1
        return dp[-1]

    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        size = len(arr)
        if size <= 1: return True
        # bfs
        queue = [start]
        visited = [False] * size
        visited[start] = True
        while len(queue) > 0:
            cur = queue.pop(0)
            if arr[cur] == 0: return True
            for val in [arr[cur], -arr[cur]]:
                next = cur + val
                if next < 0 or next > size-1: continue
                if visited[next]: continue
                visited[next] = True
                queue.append(next)
        return False





if __name__ == "__main__":
    s = Solution()

    arr = [4, 2, 3, 0, 3, 1, 2]; start = 5
    arr=[0, 3, 0, 6, 3, 3, 4]; start=6
    res = s.canReach(arr, start)
    print("can reach:", res)
    '''
    nums = [3, 2, 1, 0, 4] # False
    nums = [2, 3, 1, 1, 4] # True
    res = s.canJump(nums)
    res = s.jump(nums)
    print("can jump:", res)
    '''

    '''
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = [[1,2,3],[4,5,6]]
    res = s.minPathSum(grid)
    print("min path sum:", res)
    '''

