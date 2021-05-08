def dfs2(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    is_border = False
    for direct in directions:
        ni = i + direct[0]
        nj = j + direct[1]
        if ni<0 or nj<0 or ni>=m or nj>=n: 
            is_border = True
            continue
        if grid[ni][nj] == 0: 
            is_border = True
            continue
        if grid[ni][nj] in [2, 3]:
            continue
        grid[ni][nj] = 3
        dfs2(grid, ni, nj)
    if is_border == True:
        grid[i][j] = 2

'''
0: water,
1: island
2: is island, visited, border of island
3: is island, visited, not border

border island: 1-->3-->2
not border: 1-->3-->1
'''

def set_border(grid):
    m = len(grid)
    if m <= 0: return 0
    n = len(grid[0])
    if n<= 0: return 0
    count = 0; visited = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 3
                dfs2(grid, i, j)
                count += 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 3:
                grid[i][j] = 1


grid = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0, 0, 1],
[0, 1, 1, 1, 1, 0, 1, 1],
[0, 0, 1, 1, 1, 0, 1, 1,],
[0, 0, 0, 0, 0, 0, 0, 0]
]

set_border(grid)
for val in grid:
    print(val)


