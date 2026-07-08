from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificborders = set()
        atlanticborders = set()


        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0:
                    pacificborders.add((r,c))
                if c == 0:
                    pacificborders.add((r,c))
                if r == len(heights)-1:
                    atlanticborders.add((r,c))
                if c == len(heights[0])-1:
                    atlanticborders.add((r,c))

        atlqueue = deque()
        for i in atlanticborders:
            atlqueue.append(i)
        
        visited = set()
        while atlqueue:
            current = atlqueue.popleft()
            if current not in visited:
                visited.add(current)
                atlanticborders.add(current)
                x,y = current
                neighbors = []
                if x+1 < len(heights) and heights[x+1][y] >= heights[x][y]:
                    neighbors.append((x+1, y))
                if x-1 >= 0 and heights[x-1][y] >= heights[x][y]:
                    neighbors.append((x-1, y))
                if y-1 >= 0 and heights[x][y-1] >= heights[x][y]:
                    neighbors.append((x, y-1))
                if y+1 < len(heights[0]) and heights[x][y+1] >= heights[x][y]:
                    neighbors.append((x, y+1))
            for neighbor in neighbors:
                if neighbor not in visited:
                    atlqueue.append(neighbor)


        print(atlanticborders)
        pacqueue = deque()
        for i in pacificborders:
            pacqueue.append(i)
        pvisited = set()

        while pacqueue:
            current = pacqueue.popleft()
            if current not in pvisited:
                pvisited.add(current)
                pacificborders.add(current)
                x,y = current
                neighbors = []
                if x+1 < len(heights) and heights[x+1][y] >= heights[x][y]:
                    neighbors.append((x+1, y))
                if x-1 >= 0 and heights[x-1][y] >= heights[x][y]:
                    neighbors.append((x-1, y))
                if y-1 >= 0 and heights[x][y-1] >= heights[x][y]:
                    neighbors.append((x, y-1))
                if y+1 < len(heights[0]) and heights[x][y+1] >= heights[x][y]:
                    neighbors.append((x, y+1))
            for neighbor in neighbors:
                if neighbor not in pvisited:
                    pacqueue.append(neighbor)

        print(pacificborders)


        result = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacificborders and (r,c) in atlanticborders:
                    result.append([r,c])
        return result


        