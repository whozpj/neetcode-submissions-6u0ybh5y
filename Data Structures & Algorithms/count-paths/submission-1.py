class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        c = m
        r = n

        grid = [[0] * c for _ in range(r)]

        #set the bottom all to 1
        for i in range(c):
            grid[n-1][i] = 1

        #set right all to 1:
        for row in range(r):
            grid[row][c - 1] = 1

        for row in range(r-2, -1, -1):
            for col in range(c-2,-1,-1):

                down = 0
                right = 0

                if col + 1 <= c -1:
                    right = grid[row][col+1]
                if row + 1 <= r -1:
                    down = grid[row+1][col]

                grid[row][col] = right + down

        return grid[0][0]
        