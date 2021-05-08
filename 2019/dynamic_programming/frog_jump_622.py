class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def helper(self, stones, n_map, pos, k):
        n = len(stones)
        key = pos | k << 11
        if pos >= n-1: return True
        if key in n_map: return n_map[key]
        for i in range(pos+1, n):
            dist = stones[i] - stones[pos]
            if dist < k - 1: continue
            if dist > k + 1:
                n_map[key] = False
                return False
            if self.helper(stones, n_map, i, dist):
                n_map[key] = True
                return True
        n_map[key] = False
        return False

    # DFS + mem
    def canCross(self, stones):
        # write your code here
        n_map = {}
        return self.helper(stones, n_map, 0, 0)

s = Solution()
stones = [0,1,3,5,6,8,12,17]
print(s.canCross(stones))
