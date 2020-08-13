class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    perimeter = perimeter + 4
                    if(i > 0):
                        if(grid[i-1][j] and grid[i-1][j] == 1):
                            perimeter = perimeter - 1
                    if(i < m - 1):
                        if(grid[i+1][j] and grid[i+1][j] == 1):
                            perimeter = perimeter - 1
                    if(j > 0):
                        if(grid[i][j-1] and grid[i][j-1] == 1):
                            perimeter = perimeter - 1
                    if(j < n - 1):
                        if(grid[i][j+1] and grid[i][j+1] == 1):
                            perimeter = perimeter - 1   
        return perimeter