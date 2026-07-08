class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right-left):

                top, bottom = left, right

                topLeft = matrix[top][left+i]

                #move bottom left to top left:
                matrix[top][left+i] = matrix[bottom-i][left]

                #move bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]

                #move top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]

                #move top left to top right - stored at beginning
                matrix[top+i][right] = topLeft

            left += 1
            right -= 1






        '''
        #we need to flip all the rows, so top becomes bottom, etc
        #then we need to make the rows the cols and the cols the rows

        #flip

        matrix.reverse()


        #make the rows and colums swithc

        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
'''

