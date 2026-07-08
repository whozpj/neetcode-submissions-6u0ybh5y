class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def explore(r,c,grid,visited):
            if ((r,c) in visited):
                return 0
            if not (0 <= r < len(grid)):
                return 0
            if not(0 <= c < len(grid[0])):
                return 0
            if grid[r][c] == 0:
                return 0
            visited.add((r,c))
            print(visited)
            count = 1

            count += explore(r + 1, c, grid, visited)
            count +=explore(r - 1, c, grid, visited)
            count +=explore(r, c + 1, grid, visited)
            count +=explore(r, c - 1, grid, visited)

            return count

        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                count = max(count, explore(r, c, grid, visited))
        return count


