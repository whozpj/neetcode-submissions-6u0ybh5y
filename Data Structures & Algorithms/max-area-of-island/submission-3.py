class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        maxArea = 0
        seen = set()

        def getMaxArea(r,c):
            currMax = 0

            queue = [(r,c)]
            seen.add((r,c))

            while queue:

                row,col = queue.pop(0)

                if grid[row][col] == 1:
                    currMax += 1


                    if (row+1) < len(grid) and (row+1,col) not in seen:
                        queue.append((row+1,col))
                        seen.add((row+1,col))
                    if (col+1) < len(grid[0]) and (row,col+1) not in seen:
                        queue.append((row,col+1))
                        seen.add((row,col+1))
                    if (row-1) >= 0 and (row-1,col) not in seen:
                        queue.append((row-1,col))
                        seen.add((row-1,col))
                    if (col-1) >= 0 and (row,col-1) not in seen:
                        queue.append((row,col-1))
                        seen.add((row,col-1))

            return currMax






        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row,col) not in seen:
                    maxArea = max(getMaxArea(row,col), maxArea)


        return maxArea