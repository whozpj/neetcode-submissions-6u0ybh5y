class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        seen = set()

        def checkPerimeter(row, col):
            
            perimeter = 0
            if row + 1 >= len(grid):
                perimeter += 1
            elif grid[row+1][col] == 0:
                perimeter += 1

            if col + 1 >= len(grid[0]):
                perimeter += 1
            elif grid[row][col+1] == 0:
                perimeter += 1

            if row - 1 < 0:
                perimeter += 1
            elif grid[row-1][col] == 0:
                perimeter += 1

            if col - 1 < 0:
                perimeter += 1
            elif grid[row][col-1] == 0:
                perimeter += 1

            return perimeter

        def bfs(row,col):

            queue = deque()
            queue.append((row,col))
            iterResult = 0
            seen.add((row,col))

            while queue:
                r,c = queue.pop()
                
                iterResult += checkPerimeter(r,c)

                if r + 1 < len(grid) and (r+1,c) not in seen and grid[r+1][c] == 1:
                    queue.append((r+1, c))
                    seen.add((r+1,c))
                if r - 1 >= 0 and (r-1,c) not in seen and grid[r-1][c] == 1:
                    queue.append((r-1, c))
                    seen.add((r-1,c))
                if c + 1 < len(grid[0]) and (r,c+1) not in seen and grid[r][c+1] == 1:
                    queue.append((r, c + 1))
                    seen.add((r,c+1))
                if c - 1 >= 0 and (r,c-1) not in seen and grid[r][c-1] == 1:
                    queue.append((r, c-1))
                    seen.add((r,c-1))

            return iterResult
                



        result = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs(r,c)
            