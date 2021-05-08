Given a grid consisting of '0's(Water) and '1's(Land). Find the number of islands.
Note: An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically (4 directions.)






case 1: 
0 1
1 0
1 1
1 0

Answer: 2


0 1 1 1 0 0 1
0 0 1 1 1 1 1

Answer: 1


0 0 0 0 0 0 0
0 1 1 1 0 0 1
0 1 1 1 0 1 1
0 0 1 1 0 1 1
0 0 0 0 0 0 0

Answer: 2





follow up 1: want to put fance on the border of each island 



input 
0 0 0 0 0 0 0 0
0 1 1 1 1 0 0 1
0 1 1 1 1 0 1 1
0 0 1 1 1 0 1 1
0 0 0 0 0 0 0 0


output:
0 0 0 0 0 0 0 0
0 2 2 2 2 0 0 2
0 2 1 1 2 0 2 2
0 0 2 2 2 0 2 2
0 0 0 0 0 0 0 0




depth first search

def dfs(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    directions = [[0,1], [0,-1], [1,0], [-1,0]]
    for direct in directions:
        ni = i + direct[0]
        nj = j + direct[1]
        if ni<0 or nj<0 or ni>=m or nj>=n: continue
        if grid[ni][nj] != 1: continue
        grid[nj][nj] = 2
        self.dfs(grid, ni, nj)
    

def num_island(grid):
    m = len(grid)
    if m <= 0: return 0
    n = len(grid[0])
    if n<= 0: return 0
    count = 0; visited = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                self.dfs(grid, i, j)
                count += 1
     return count


0 1 1 1 0 0 1
0 0 1 1 1 1 1
m=2
n=7
i,j=0-(m-1),0-(n-1)
i,j=0,0
    0,1: grid[0][1] = 2, 
         dfs(grid, 0,1): 
             for direct =[0,1]; ni=0,nj=2; grid[0][2]=2, dfs(grid, 0, 2)
             dfs(grid, 0, 2):
                  
  time complexity: O(m*n)
  space   : O(1) --> O(m*n)


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
        if grid[ni][nj] != 1: 
            is_border = True
            continue
        grid[ni][nj] = 3
        self.dfs(grid, ni, nj)
     if grid[ni][nj]==3 and is_border = True:
         grid[nj][nj] = 2:
         
0: water,
1: island
2: is island, visited, border of island
3: is island, visited, not border

border island: 1-->3-->2
not border: 1-->3-->1

def func(grid):
    m = len(grid)
    if m <= 0: return 0
    n = len(grid[0])
    if n<= 0: return 0
    count = 0; visited = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[ni][nj] = 3
                self.dfs2(grid, i, j)
                count += 1
     for i in range(m):
        for j in range(n):
            if grid[i][j] == 3:
                grid[i][j] == 1
     return count


