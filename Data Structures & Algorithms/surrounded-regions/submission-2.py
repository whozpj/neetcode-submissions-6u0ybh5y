class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #go through each border number until you see a O. if there is a O, then
        #run dfs and save the 0s in a set. Then at the end, turn the whole thing
        #into an x except the 0s

        bad = set()
        
        def explore(r,c,board,bad):
            if board[r][c] == 'O' and (r,c) not in bad:
                bad.add((r,c))
                if r+1 <=len(board)-1:
                    explore(r+1,c,board,bad)
                if r-1 >= 0:
                    explore(r-1,c,board,bad)
                if c+1 <=len(board[0])-1:
                    explore(r,c+1,board,bad)
                if c-1 >=0:
                    explore(r,c-1,board,bad)
            return



        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    if board[r][c] == 'O':
                        explore(r,c,board,bad)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) not in bad:
                    board[r][c] = 'X'

        



        
                    