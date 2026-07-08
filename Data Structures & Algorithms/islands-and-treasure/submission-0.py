from collections import deque
class Solution:
    def explore(self, r,c,grid):
        queue = deque()
        distance = 0
        queue.append((r,c))
        visited = set()
        while queue:
            currentlength = len(queue)
            for i in range(currentlength):
                neighbors = []
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    x,y = current
                    if grid[x][y] == 0:
                        return distance
                    if current[0] +1 < len(grid):
                        neighbors.append((current[0]+1, current[1]))
                    if current[0] -1 >= 0:
                        neighbors.append((current[0]-1, current[1]))
                    if current[1] -1 >= 0:
                        neighbors.append((current[0], current[1]-1))
                    if current[1] +1 < len(grid[0]):
                        neighbors.append((current[0], current[1]+1))
                    
                    for nr,nc in neighbors:
                        if grid[nr][nc] != -1:
                            queue.append((nr,nc))
            distance += 1

        return 2147483647

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2147483647:
                    grid [r][c] = self.explore(r,c,grid)
                

