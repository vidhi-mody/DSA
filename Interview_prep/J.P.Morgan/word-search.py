#Given an m x n grid of characters board and a string word, return true if word exists in the grid.

#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
#The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtrack(i, j, idx):
            char = board[i][j]
            if(char != word[idx]):
                return False
            elif(idx == len(word)-1):
                return True
            
            board[i][j] = ''
            
            if(i > 0 and backtrack(i-1, j, idx+1)):
                return True
            if(j > 0 and backtrack(i, j-1, idx+1)):
                return True
            if(i < rows-1 and backtrack(i+1, j, idx+1)):
                return True
            if(j < cols-1 and backtrack(i, j+1, idx+1)):
                return True            
            board[i][j] = char
            return False
                    
        for i in range(rows):
            for j in range(cols):
                if(backtrack(i, j, 0)):
                    return True
            
        return False
        