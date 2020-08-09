class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        M = len(grid)
        N = len(grid[0])
        def findConnection(row, col):
            if(grid[row][col] == "1"):
                grid[row][col] = "0"
                if row > 0 :
                    findConnection(row-1,col)
                if row < M-1 :
                    findConnection(row+1,col)
                if col > 0 :
                    findConnection(row,col-1)
                if col < N-1 :
                    findConnection(row,col+1)
        count = 0
        for i in range(M):
            for j in range(N):
                if(grid[i][j]=="1"):
                    findConnection(i,j)
                    count = count + 1
        return count