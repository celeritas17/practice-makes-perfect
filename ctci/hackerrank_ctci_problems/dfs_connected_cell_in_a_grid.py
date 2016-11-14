def get_neighbors(grid, row, col, n, m):
    neighbors = []
    next_row = 1 if row < n - 1 else 0
    last_row = 1 if row > 0 else 0
    next_col = 1 if col < m - 1 else 0
    last_col = 1 if col > 0 else 0

    neighbors = [
        (row - last_row, col),
        (row - last_row, col - last_col),
        (row - last_row, col + next_col),
        (row, col + next_col),
        (row, col - last_col),
        (row + next_row, col),
        (row + next_row, col - last_col),
        (row + next_row, col + next_col)
    ]
    
    neighbors = set([cell for cell in neighbors if grid[cell[0]][cell[1]]])
    if (row, col) in neighbors: neighbors.remove((row, col))
    return neighbors

def DFS_region(grid, explored, row, col):
    size = 1
    explored[row][col] = True
    neighbors = get_neighbors(grid, row, col, len(grid), len(grid[0]))
    for cell in neighbors:
        i, j = cell
        if not explored[i][j]:
            explored[i][j] = True
            size += DFS_region(grid, explored, i, j)
    
    return size

'''
(!)(!)(!) Had two bugs in this function:

          (1) Tried to be cute while creating the 'explored' matrix
              and had a weird bug where entire columns were being 
              set to True when I tried to set one entry to True.
              Lesson: Just create such things in the straightforward
              way.
          
          (2) Initially had largest_region += DFS_region(grid, explored, i, j)
              instead of appending DFS_region result to array. This resulted 
              in a sum of all of the regions in the input array, so it got the 
              right answer if there was only one region in the input array.
'''
def getBiggestRegion(grid):
    regions = []
    explored = []
    
    for i in range(len(grid)):
        explored.append([])
        for j in range(len(grid[0])):
            explored[i].append(False)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not explored[i][j]:
                regions.append(DFS_region(grid, explored, i, j)) 
    
    return max(regions)
    
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
