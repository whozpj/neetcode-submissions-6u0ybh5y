class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = []
        seen = set()

        def addRooms(r,c):

            if (r+1)<len(grid) and (r+1,c) not in seen and grid[r+1][c] == 2147483647: 
                queue.append((r+1,c))
                seen.add((r+1,c))
            if (c+1)<len(grid[0]) and (r,c+1) not in seen and grid[r][c+1] == 2147483647: 
                queue.append((r,c+1))
                seen.add((r,c+1))
            if (r-1) >= 0  and (r-1,c) not in seen and grid[r-1][c] == 2147483647: 
                queue.append((r-1,c))
                seen.add((r-1,c))
            if (c-1) >= 0  and (r,c-1) not in seen and grid[r][c-1] == 2147483647: 
                queue.append((r,c-1))
                seen.add((r,c-1))





        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row,col))
                    seen.add((row,col))
        
        distance = 0
        
        while queue:
            for i in range(len(queue)):
                row,col = queue.pop(0)
                grid[row][col] = distance
                addRooms(row,col)
            distance += 1



                






        