from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            numbersList = []
            for column in range(len(board)):
                if board[row][column] != '.':
                    numbersList.append(board[row][column])
            if len(set(numbersList)) < len(numbersList):
                return False

        for column in range(len(board)):
            numbersList = []
            for row in range(len(board)):
                if board[row][column] != '.':
                    numbersList.append(board[row][column])
            if len(set(numbersList)) < len(numbersList):
                return False
        
        runningdict = defaultdict(list)
        for row in range(len(board)):
            bigrow = row//3
            for col in range(len(board)):
                if board[row][col] != '.':
                    runningdict[(row//3,col//3)].append(board[row][col])
        
        for i, j in runningdict:
            if len(set(runningdict[(i,j)])) < len(runningdict[(i,j)]):
                return False

        return True
                

                    
