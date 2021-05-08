'''
we can walk over the street.
For each street, we use a dictionary to
    denote the direction to enter it, and
    the direction it leads to.
for street 1, we can enter into if previous direction is 'left',
which means we enter into it from left side, and it leads to 'left'.
if the direction not in street.keys, it means this rood is not connecteed.
so we can walk throught id.
I will set grid[x][y] to 0 while walking over,
after I finish walking over, I will set grid[x][y] to -1.

'''


class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        node_map = {
            1: [[], [1,3,5], [], [1,4,6]],
            2: [[2, 3, 4], [], [2,5,6], []],
            3: [[], [], [2,5,6], [1,4,6]],
            4: [[], [1,3,5], [2,5,6], []],
            5: [[2,3,4], [], [], [1,4,6]],
            6: [[2,3,4], [1,3,5], [], []]
        }
        if len(grid) <= 0: return False
        return self.dfs(node_map, grid, 0, 0)


    def dfs(self, node_map, grid, x, y):
        print('start', x, y, grid[x][y])
        if grid[x][y] <= 0: return False
        m = len(grid)
        n = len(grid[0])
        if x == m-1 and y == n-1: return True
        directs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        mapping = node_map[grid[x][y]]
        grid[x][y] = 0
        for i in range(4):
            nx = x + directs[i][0]
            ny = y + directs[i][1]
            if nx < 0 or nx>=m or ny < 0 or ny >= n: continue
            print("check next", nx, ny, grid[nx][ny], i, mapping[i], directs[i])
            if grid[nx][ny] in mapping[i] and grid[nx][ny]>0:
                print('next', nx, ny, grid[nx][ny], i, mapping[i])
                if self.dfs(node_map, grid, nx, ny): return True
        grid[x][y] = -1
        print('end', x, y, grid[x][y])
        return False


s = Solution()
grid = [[2,4,3],[6,5,2]] # True
grid = [[1,2,1],[1,2,1]] # False
grid = [[1,1,2]] # False
grid = [[1,1,1,1,1,1,3]] # True
grid = [[2],[2],[2],[2],[2],[2],[6]] # True
res = s.hasValidPath(grid)
print(res)