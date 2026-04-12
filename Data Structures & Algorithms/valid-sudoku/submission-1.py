class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for column in range(len(board)):
                if board[row][column] != '.':
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])

        for column in range(len(board)):
            seen = set()
            for row in range(len(board)):
                if board[row][column] != '.':
                    if board[row][column] in seen:
                        return False
                    seen.add(board[row][column])

        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                seen = set()
        
                for i in range(3):
                    for j in range(3):
                        val = board[boxRow + i][boxCol + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)

        return True



