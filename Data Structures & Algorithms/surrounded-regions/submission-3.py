class Solution:
    def solve(self, board: List[List[str]]) -> None:

        queue = deque()


        for row in range(len(board)):
            if board[row][0] == 'O':
                board[row][0] = 'S'
                queue.append((row,0))
            if board[row][len(board[0])-1] == 'O':
                board[row][len(board[0])-1] = 'S'
                queue.append((row,len(board[0])-1))

        for col in range(len(board[0])):
            if board[0][col] == 'O':
                board[0][col] = 'S'
                queue.append((0,col))
            if board[len(board)-1][col] == 'O':
                board[len(board)-1][col] = 'S'
                queue.append((len(board)-1, col))

        while queue:

            row,col = queue.popleft()
            board[row][col] = 'S'

            if row + 1 < len(board) and board[row+1][col] == 'O': queue.append((row+1,col))
            if col + 1 < len(board[0]) and board[row][col+1] == 'O': queue.append((row,col+1))
            if row -1 >= 0 and board[row-1][col] == 'O': queue.append((row-1,col))
            if col -1 >= 0 and board[row][col-1] == 'O': queue.append((row,col-1))


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'S':
                    board[row][col] = 'O'
                    



