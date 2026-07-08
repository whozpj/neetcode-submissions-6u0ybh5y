class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        seen = set()
        result = 0

        def search(row,col):

            if grid[row][col] != '1' or (row,col) in seen:
                return

            seen.add((row,col))
            if (row + 1) < len(grid): search(row+1, col)
            if (row - 1) >= 0: search(row-1, col)
            if (col + 1) < len(grid[0]): search(row, col+1)
            if (col- 1) >= 0: search(row, col-1)



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row,col) not in seen:
                    result += 1
                    search(row , col)

        return result