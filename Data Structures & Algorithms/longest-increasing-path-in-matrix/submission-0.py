class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        


        memo = {}

        def search(row, col):

            if (row, col) in memo:
                return memo[(row,col)]

            largestPath = 1

            if row + 1 < len(matrix) and matrix[row+1][col] > matrix[row][col]:
                largestPath = max(largestPath, 1 + search(row+1, col))
            if col + 1 < len(matrix[0]) and matrix[row][col+1] > matrix[row][col]:
                largestPath = max(largestPath,1 + search(row, col+1))


            if row - 1 >= 0 and matrix[row-1][col] > matrix[row][col]:
                largestPath = max(largestPath,1 + search(row-1, col))
            if col - 1 >= 0 and matrix[row][col-1] > matrix[row][col]:
                largestPath = max(largestPath,1 + search(row, col-1))



            memo[(row,col)] = largestPath
            return largestPath

        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, search(r,c))

        return maxPath
