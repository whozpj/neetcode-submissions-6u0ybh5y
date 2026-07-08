class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, index, seen):

            #went one past after finding word
            if index == len(word):
                return True

            if row < 0 or col < 0 or row > ROWS-1 or col > COLS-1:
                return False

            #main check
            if board[row][col] != word[index]:
                return False
            
            if (row,col) in seen:
                return False
            
            seen.add((row,col))

            result = (
            dfs(row + 1, col, index+1, seen) or
            dfs(row, col + 1, index+1, seen) or
            dfs(row - 1, col , index+1, seen) or
            dfs(row, col - 1, index+1, seen))
            
            seen.remove((row,col))
            return result


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, set()):
                    return True
        return False


            

