class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        flowsIntoPacific = set()
        flowsIntoAtlantic = set()

        def searchPacific(r,c):
            flowsIntoPacific.add((r,c))

            queue = deque()
            queue.append((r,c))

            while queue:

                row,col = queue.popleft()

                if (row+1 < len(heights)) and ((row+1,col) not in flowsIntoPacific) and (heights[row][col] <= heights[row+1][col]):
                    queue.append((row+1,col))
                    flowsIntoPacific.add((row+1,col))
                if (col+1 < len(heights[0])) and ((row,col+1) not in flowsIntoPacific) and (heights[row][col] <= heights[row][col+1]):
                    queue.append((row,col+1))
                    flowsIntoPacific.add((row,col+1))
                if (row-1 >= 0) and ((row-1,col) not in flowsIntoPacific) and (heights[row][col] <= heights[row-1][col]):
                    queue.append((row-1,col))
                    flowsIntoPacific.add((row-1,col))
                if (col-1 >= 0) and ((row,col-1) not in flowsIntoPacific) and (heights[row][col] <= heights[row][col-1]):
                    queue.append((row,col-1))
                    flowsIntoPacific.add((row,col-1))




        def searchAtlantic(r,c):
            flowsIntoAtlantic.add((r,c))

            queue = deque()
            queue.append((r,c))

            while queue:

                row,col = queue.popleft()
                
                if (row+1 < len(heights)) and ((row+1,col) not in flowsIntoAtlantic) and (heights[row][col] <= heights[row+1][col]):
                    queue.append((row+1,col))
                    flowsIntoAtlantic.add((row+1,col))
                if (col+1 < len(heights[0])) and ((row,col+1) not in flowsIntoAtlantic) and (heights[row][col] <= heights[row][col+1]):
                    queue.append((row,col+1))
                    flowsIntoAtlantic.add((row,col+1))
                if (row-1 >= 0) and ((row-1,col) not in flowsIntoAtlantic) and (heights[row][col] <= heights[row-1][col]):
                    queue.append((row-1,col))
                    flowsIntoAtlantic.add((row-1,col))
                if (col-1 >= 0) and ((row,col-1) not in flowsIntoAtlantic) and (heights[row][col] <= heights[row][col-1]):
                    queue.append((row,col-1))
                    flowsIntoAtlantic.add((row,col-1))

        for row in range(len(heights)):
            searchPacific(row, 0)
            searchAtlantic(row,len(heights[0])-1)
        for col in range(len(heights[0])):
            searchPacific(0,col)
            searchAtlantic(len(heights)-1, col)

        result = []

        for r, c in flowsIntoPacific:
            if (r, c) in flowsIntoAtlantic:
                result.append([r, c])

        return result