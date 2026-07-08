class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()


        def dfs(row,col,index):

            if index == len(word):
                return True
            if ((row,col)) in seen:
                return False
            

            if (0 <= row < len(board)) and (0 <= col < len(board[0])) and (row,col) not in seen:

                if board[row][col] != word[index]:
                    return False

                seen.add((row,col))
                
                if dfs(row+1,col,index + 1) or dfs(row, col+1, index + 1) or dfs(row-1,col,index+1) or dfs(row,col-1,index + 1):
                    seen.remove((row,col))
                    return True
                else:
                    seen.remove((row,col))
                    return False
            return False

            
            



        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0):
                        return True
        return False
