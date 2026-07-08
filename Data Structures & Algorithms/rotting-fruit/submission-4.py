class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        #append the rotten fruit to the queue
        #at each bfs stage, increase the time
        #after we are done, run a loop over the grid to see if there are rotten fruit left



        seen = set()
        queue = deque()

        if grid == [[0]]:
            return 0

        def addFruits(r,c):

            if (r+1)<len(grid) and (r+1,c) not in seen and grid[r+1][c] == 1: 
                queue.append((r+1,c))
                seen.add((r+1,c))
            if (c+1)<len(grid[0]) and (r,c+1) not in seen and grid[r][c+1] == 1: 
                queue.append((r,c+1))
                seen.add((r,c+1))
            if (r-1) >= 0  and (r-1,c) not in seen and grid[r-1][c] == 1: 
                queue.append((r-1,c))
                seen.add((r-1,c))
            if (c-1) >= 0  and (r,c-1) not in seen and grid[r][c-1] == 1: 
                queue.append((r,c-1))
                seen.add((r,c-1))
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                    seen.add((row,col))

        time = -1

        while queue:
            for i in range(len(queue)):
                row,col = queue.popleft()
                grid[row][col] = 2
                addFruits(row,col)
            time += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1

        if time == -1:
            return 0
        return time

        