from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque()
        largestLength = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        if len(queue) == 0:
            for row in grid:
                if 1 in row:
                    return -1
            return 0
        visited = set()
        while queue:
                currentlayer = len(queue)
                for i in range(currentlayer):
                    current = queue.popleft()
                    if current not in visited:
                        visited.add(current)
                        neighbors = []
                        if current[0] +1 < len(grid):
                            neighbors.append((current[0]+1, current[1]))
                        if current[0] -1 >= 0:
                            neighbors.append((current[0]-1, current[1]))
                        if current[1] -1 >= 0:
                            neighbors.append((current[0], current[1]-1))
                        if current[1] +1 < len(grid[0]):
                            neighbors.append((current[0], current[1]+1))
                        for nr, nc in neighbors:
                            if grid[nr][nc] == 1:
                                grid[nr][nc] = 2
                                queue.append((nr,nc))
                minutes += 1

        for row in grid:
            if 1 in row:
                return -1
        
        
        return minutes - 1
            